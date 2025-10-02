# This file is part of invocation_tree.
# Copyright (c) 2023, Bas Terwijn.
# SPDX-License-Identifier: BSD-2-Clause

from graphviz import Digraph
import html
import sys
import difflib 

import invocation_tree.regex_set as regset

__version__ = "0.0.32"
__author__ = 'Bas Terwijn'

def highlight_diff(str1, str2):
    matcher = difflib.SequenceMatcher(None, str1, str2)
    result = []
    is_highlighted = False
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == 'replace':
            result.append(f'<B>{str2[j1:j2]}&#8203;</B>&#8203;')
            is_highlighted = True
        elif tag == 'delete':
            result.append(f'<FONT COLOR="#aaaaaa"><S>{str1[i1:i2]}&#8203;</S></FONT>&#8203;')
            is_highlighted = True
        elif tag == 'insert':
            result.append(f'<B>{str2[j1:j2]}&#8203;</B>&#8203;')
            is_highlighted = True
        elif tag == 'equal':
            result.append(str2[j1:j2])
    diff = ''.join(result)
    return diff, is_highlighted

def get_class_function_name(frame):
    class_name = ''
    if 'self' in frame.f_locals:
        class_name = frame.f_locals['self'].__class__.__name__ + '.'
    function_name = class_name+frame.f_code.co_name
    return function_name

def filter_variables(var, val):
    if callable(val):
        return False
    if isinstance(val, (type, type(object), type(__import__('os')))):
        return False
    if var.startswith('__'):
        return False
    return True

class Tree_Node:

    def __init__(self, node_id, frame, return_value):
        self.node_id = node_id
        self.frame = frame
        self.return_value = return_value
        self.is_returned = False
        self.strings = {}

    def __repr__(self):
        return f'node_id:{self.node_id} frame:{self.frame} return_value:{self.return_value}'

class Invocation_Tree:

    def __init__(self, 
                 filename='tree.pdf',
                 render=True,
                 show=True, 
                 block=True, 
                 src_loc=True, 
                 each_line=False, 
                 gifcount=-1,
                 max_string_len=150, 
                 indent='   ', 
                 color_paused = '#ccffcc', 
                 color_active = '#ffffff', 
                 color_returned = '#ffcccc', 
                 to_string=None, 
                 hide_vars=None,
                 cleanup=True,
                 quiet=True):
        # --- config
        self.filename = filename
        self.prev_filename = None
        self.render = render
        self.show = show
        self.block = block
        self.src_loc = src_loc
        self.max_string_len = max_string_len
        self.gifcount = gifcount
        self.indent = indent
        self.color_paused = color_paused
        self.color_active = color_active
        self.color_returned = color_returned
        self.each_line = each_line
        self.to_string = {}
        if not to_string is None:
            self.to_string = to_string
        self.hide_vars = set()
        if not hide_vars is None:
            self.hide_vars = hide_vars
        self.cleanup = cleanup
        self.quiet = quiet
        self.hide_calls = {'Invocation_Tree.__exit__', 'Invocation_Tree.stop_trace', '<genexpr>'}
        self.ignore_calls = set()
        self.ignoring_call = None
        self.regset_hide_vars = regset.Regex_Set(self.hide_vars)
        self.regset_hide_calls = regset.Regex_Set(self.hide_calls)
        self.regset_ignore_calls = regset.Regex_Set(self.ignore_calls)
        self.fontname = 'Courier'
        self.fontsize = '14'
        # --- core
        self.stack = []
        self.returned = []
        self.prev_returned = []
        self.paused = []
        self.prev_paused = []
        self.node_id = 0
        self.node_id_to_table = {}
        self.edges = []
        self.is_highlighted = False
        self.graph = None
        self.prev_global_tracer = None
        

    def __repr__(self):
        return f'Invocation_Tree(filename={repr(self.filename)}, show={self.show}, block={self.block}, each_line={self.each_line}, gifcount={self.gifcount})'

    def __call__(self, fun, *args, **kwargs):
        try:
            self.prev_global_tracer = sys.gettrace()
            sys.settrace(self.global_tracer)
            result = fun(*args, **kwargs)
        finally:
            sys.settrace(self.prev_global_tracer)
        return result

    def value_to_string(self, key, value, use_repr=False):
        try:
            if id(value) in self.to_string:
                val_str = self.to_string[id(value)](value)
            elif key in self.to_string:
                val_str = self.to_string[key](value)
            elif type(value) in self.to_string:
                val_str = self.to_string[type(value)](value)
            else:
                val_str = repr(value) if use_repr else str(value)
        except Exception as e:
            val_str = '<not-string-convertable>'
        if len(val_str) > self.max_string_len:
            val_str = '...'+val_str[-self.max_string_len:]
        return html.escape(val_str)

    def get_hightlighted_content(self, tree_node, key, value, use_old_content=False, use_repr=False):
        if use_old_content and key in tree_node.strings:
            return tree_node.strings[key]
        is_highlighted = False
        content = self.value_to_string(key, value, use_repr=use_repr)
        if key in tree_node.strings:
            use_old_content = tree_node.strings[key]
            hightlighted_content, is_highlighted = highlight_diff(use_old_content, content)
        else:
            if len(content.strip())>0: # fixes graphviz error on empty <B></B> tag
                hightlighted_content = '<B>'+content+'</B>' 
                is_highlighted = True
            else:
                hightlighted_content = content
        tree_node.strings[key] = content
        self.is_highlighted |= is_highlighted
        return hightlighted_content
    
    def build_html_table(self, tree_node, active=False, is_returned=None, use_old_content=False):
        if is_returned is None:
            is_returned = tree_node.is_returned
        else:
            tree_node.is_returned = is_returned
        return_value = tree_node.return_value
        border = 1
        color = self.color_paused
        if active:
            color = self.color_active
            border = 3
        if is_returned:
            color = self.color_returned
        table = f'<\n<TABLE BORDER="{str(border)}" CELLBORDER="0" CELLSPACING="0" BGCOLOR="{color}">\n  <TR>'
        class_fun_name = get_class_function_name(tree_node.frame)
        local_vars = tree_node.frame.f_locals
        hightlighted_content = self.get_hightlighted_content(tree_node, class_fun_name, class_fun_name, use_old_content)
        table += '<TD ALIGN="left">'+ '➤'+ hightlighted_content +'</TD>'
        for var,val in local_vars.items():
            var_name = class_fun_name+'..'+var
            val_name = class_fun_name+'.'+var
            if filter_variables(var,val) and not self.regset_hide_vars.match(val_name, self.hide_vars):
                table += '</TR>\n  <TR>'
                hightlighted_var = self.get_hightlighted_content(tree_node, var_name, var, use_old_content)
                hightlighted_val = self.get_hightlighted_content(tree_node, val_name, val, use_old_content, use_repr=True)
                hightlighted_content = self.indent + hightlighted_var + ': ' + hightlighted_val
                table += '<TD ALIGN="left">'+ hightlighted_content  +'</TD>'
        if is_returned:
            return_name = class_fun_name+'.return'
            if not self.regset_hide_vars.match(return_name, self.hide_vars):
                table += '</TR>\n  <TR>'
                hightlighted_content = self.get_hightlighted_content(tree_node, return_name, return_value, use_old_content, use_repr=True)
                table += '<TD ALIGN="left">'+ 'return ' + hightlighted_content +'</TD>'
        table += '</TR>\n</TABLE>>'
        return table

    def update_node(self, tree_node, active=False, returned=None, use_old_content=False):
        table = self.build_html_table(tree_node, active, returned, use_old_content=use_old_content)
        self.node_id_to_table[str(tree_node.node_id)] = table
        
    def add_edge(self, tree_node1, tree_node2):
        self.edges.append((str(tree_node1.node_id), str(tree_node2.node_id)))

    def get_output_filename(self):
        if self.gifcount >= 0:
            splits = self.filename.split('.')
            if len(splits)>1:
                splits[-2]+=str(self.gifcount)
                self.gifcount += 1
                return '.'.join(splits)
        return self.filename
        
    def create_graph(self):
        graphviz_graph_attr = {'fontname': self.fontname, 'fontsize': str(self.fontsize)}
        graphviz_node_attr = {'fontname': self.fontname, 'fontsize': str(self.fontsize), 'shape':'plaintext'}
        graphviz_edge_attr = {'fontname': self.fontname, 'fontsize': str(self.fontsize)}
        graph = Digraph('invocation_tree',
                graph_attr=graphviz_graph_attr,
                node_attr=graphviz_node_attr,
                edge_attr=graphviz_edge_attr)
        # update returned nodes
        for node in self.prev_returned:
            self.update_node(node, use_old_content=True)
        self.prev_returned = []
        for node in self.returned:
            self.update_node(node, returned=True)
            self.prev_returned.append(node)
        self.returned = []
        # update active node
        active_node = None 
        if len(self.stack)>0:
            active_node = self.stack[-1]
            self.update_node(active_node, active=True)
        # update paused nodes
        for node in self.prev_paused:
            if node is not active_node: # don't overwrite active node
                self.update_node(node, active=False, use_old_content=True)
        self.prev_paused = self.paused.copy()
        self.paused = []
        # add nodes and edges to graph
        for nid, table in self.node_id_to_table.items():
            graph.node(nid, label=table)
        for nid1, nid2 in self.edges:
            graph.edge(nid1, nid2)
        return graph
        
    def render_graph(self, graph):
        view = (self.filename!=self.prev_filename) and self.show
        graph.render(outfile=self.get_output_filename(), view=view, cleanup=self.cleanup, quiet=self.quiet)
        self.prev_filename = self.filename

    def output_graph(self, frame, event):
        if self.block or self.gifcount >= 0:
            self.is_highlighted = False
            self.graph = self.create_graph()
            if self.is_highlighted:
                if self.render:
                    self.render_graph(self.graph)
                if self.block:
                    if self.src_loc:
                        filename = frame.f_code.co_filename
                        line_nr = frame.f_lineno
                        print(f'{event.capitalize()} at {filename}:{line_nr}', end='. ')
                    input('Press <Enter> to continue...')
        else:
            self.graph = self.create_graph()
            if self.render:
                self.render_graph(self.graph)

    def get_graph(self):
        return self.graph

    def is_external(self, frame):
        """ Returns True if the call is from an external library or builtin. """
        filename = frame.f_code.co_filename
        if ('<built-in>' in filename or
            '<frozen' in filename or
            'site-packages' in filename or   # Cross-platform: works on Windows, Mac, Linux
            'lib/python' in filename or      # Linux/Mac standard library
            'lib\\python' in filename or     # Windows standard library (backslashes)
            'Python.framework' in filename): # Mac framework Python
            return True
        return False

    def trace(self, frame, event, arg):
        if self.is_external(frame):
            return
        class_fun_name = get_class_function_name(frame)
        if event == 'return':
            if class_fun_name == self.ignoring_call:
                self.ignoring_call = None
                return
        if self.ignoring_call is not None:
            return
        if event == 'call':
            if self.regset_ignore_calls.match(class_fun_name, self.ignore_calls):
                self.ignoring_call = class_fun_name
                return
        if not self.regset_hide_calls.match(class_fun_name, self.hide_calls):
            if event == 'call':
                # update previous active node with its current frame now
                if len(self.stack)>0:
                    previous = self.stack[-1]
                    self.update_node(previous, active=False)
                    self.paused.append(previous)
                # create new node
                self.stack.append(Tree_Node(self.node_id, frame, None))
                self.node_id += 1
                if len(self.stack)>1:
                    self.add_edge(self.stack[-2], self.stack[-1])
                    self.paused.append(self.stack[-2])
                self.output_graph(frame, event)
            elif event == 'return':
                self.stack[-1].return_value = arg
                self.returned.append(self.stack.pop())
                self.output_graph(frame, event)
            elif event == 'line' and self.each_line:
                self.output_graph(frame, event)

    def global_tracer(self, frame, event, arg):
        """ Global trace function that chains to any previous global tracer so it works in a debugger too. """
        self.trace(frame, event, arg) # update graph
        # call previous global tracer if any existed
        prev_local_tracer = self.prev_global_tracer(frame, event, arg) if self.prev_global_tracer else None

        def local_tracer(frame, event, arg):
            """ Global trace is for a 'call' event that signals a new frame, it returns a local tracer to 
            handle other events in that frame. """
            self.trace(frame, event, arg)

        def local_multiplexer(frame, event, arg):
            """ Multiplexes between the local tracer and any previous local tracer so it works in a debugger too. """
            nonlocal prev_local_tracer
            local_tracer(frame, event, arg) # update graph
            if prev_local_tracer is not None:
                # call previous local tracer if any existed and update it
                prev_local_tracer = prev_local_tracer(frame, event, arg)
                if prev_local_tracer is None:
                   return None # stop tracing if debugger stopped tracing
            return local_multiplexer

        return local_multiplexer

def blocking(filename='tree.pdf'):
    return Invocation_Tree(filename=filename)

def blocking_each_change(filename='tree.pdf'):
    return Invocation_Tree(filename=filename, each_line=True)

def debugger(filename='tree.pdf'):
    return Invocation_Tree(filename=filename, show=False, block=False, each_line=True)

def debugger_no_render(filename='tree.pdf'):
    return Invocation_Tree(filename=filename, render=False, show=False, block=False, each_line=True)

def gif(filename='tree.png'):
    return Invocation_Tree(filename=filename, show=False, block=False, gifcount=0)

def gif_each_change(filename='tree.png'):
    return Invocation_Tree(filename=filename, show=False, block=False, gifcount=0, each_line=True)

def non_blocking(filename='tree.pdf'):
    return Invocation_Tree(filename=filename, block=False)

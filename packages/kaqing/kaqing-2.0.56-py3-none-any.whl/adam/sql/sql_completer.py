from typing import Callable, Iterable
from prompt_toolkit.completion import CompleteEvent, Completer, Completion
from prompt_toolkit.document import Document
import sqlparse
from sqlparse.sql import Statement, Token
from sqlparse import tokens as T

from adam.sql.term_completer import TermCompleter

columns = TermCompleter(['id', 'x.', 'y.', 'z.'])

class SqlCompleter(Completer):

    def __init__(self, tables: Callable[[], list[str]], dml: str = None, debug = False):
        super().__init__()
        self.dml = dml
        self.tables = tables
        self.debug = debug

    def get_completions(
        self, document: Document, complete_event: CompleteEvent
    ) -> Iterable[Completion]:
        text = document.text_before_cursor.lstrip()
        if self.dml:
            state = f'{self.dml}_'
            text = f'{self.dml} {text}'

        completer = None
        stmts = sqlparse.parse(text)
        if not stmts:
            completer = TermCompleter(['select', 'insert', 'delete', 'update'])
        else:
            statement: Statement = stmts[0]
            state = self.traverse_tokens(text, statement.tokens)
            if self.debug:
                print('\n  =>', state)
            if state == 'dml_incomplete':
                completer = TermCompleter(['select', 'insert', 'delete', 'update'])

            elif state == 'select_':
                completer = TermCompleter(['*'])
            elif state == 'select_a':
                completer = TermCompleter(['from'])
            elif state == 'select_a,':
                completer = TermCompleter(['*'])
            elif state == 'select_a_':
                completer = TermCompleter(['from'])
            elif state == "select_a_from_":
                completer = TermCompleter(self.tables())
            elif state == "select_a_from_x_":
                completer = TermCompleter(['as', 'where', 'inner', 'left', 'right', 'full', 'group', 'limit'])
            elif state == "select_a_from_x_as_x_":
                completer = TermCompleter(['where', 'inner', 'left', 'right', 'full', 'group', 'limit'])
            elif state == "select_a_from_x,":
                completer = TermCompleter(self.tables())
            elif state == "select_a_from_x_as_":
                completer = TermCompleter(['x', 'y', 'z'])
            elif state == "select_a_from_x_as_x,":
                completer = TermCompleter(self.tables())
            elif state == "select_a_from_x_where_":
                completer = columns
            elif state == "select_a_from_x_where_id":
                completer = TermCompleter(['=', '<', '<=', '>', '>=', '<>', 'like'])
            elif state == "select_a_from_x_where_id=":
                completer = TermCompleter(["'"])
            elif state == "select_a_from_x_where_id=v_":
                completer = TermCompleter(['and', 'or', 'group', 'limit'])
            elif state == "select_a_from_x_where_id=v_limit_":
                completer = TermCompleter(['1'])
            elif state == "select_a_from_x_group_":
                completer = TermCompleter(['by'])
            elif state == "select_a_from_x_group_by_":
                completer = columns
            elif state == "select_a_from_x_group_by_a,":
                completer = columns
            elif state == "select_a_from_x_group_by_a_":
                completer = TermCompleter(['limit'])
            elif state == "select_a_from_x_group_by_a_limit_":
                completer = TermCompleter(['1'])
            elif state == "select_a_from_x_inner_":
                completer = TermCompleter(['join'])
            elif state in ["select_a_from_x_inner_join_", "select_a_from_x_left_join_"]:
                completer = TermCompleter(self.tables())
            elif state == "select_a_from_x_inner_join_y,":
                completer = TermCompleter(self.tables())
            elif state == "select_a_from_x_inner_join_y_":
                completer = TermCompleter(['on'])
            elif state == "select_a_from_x_inner_join_y_on_":
                completer = columns
            elif state == "select_a_from_x_inner_join_y_on_a":
                completer = TermCompleter(['='])
            elif state == "select_a_from_x_inner_join_y_on_a=":
                completer = columns
            elif state == "select_a_from_x_inner_join_y_on_a=b_":
                completer = TermCompleter(['where', 'group', 'limit'])
            elif state == "select_a_from_x_left_":
                completer = TermCompleter(['outer', 'join'])
            elif state == "select_a_from_x_left_outer_":
                completer = TermCompleter(['join'])
            elif state == "select_a_from_x_right_":
                completer = TermCompleter(['outer', 'join'])
            elif state == "select_a_from_x_right_outer_":
                completer = TermCompleter(['join'])
            elif state == "select_a_from_x_full_":
                completer = TermCompleter(['outer'])
            elif state == "select_a_from_x_full_outer_":
                completer = TermCompleter(['join'])

            elif state == "insert_":
                completer = TermCompleter(['into'])
            elif state == "insert_into_":
                completer = TermCompleter(self.tables())
            elif state == "insert_into_x_":
                completer = TermCompleter(['values'])
            elif state == "insert_into_x(":
                completer = columns
            elif state == "insert_into_x(a,":
                completer = columns
            elif state == "insert_into_x(a)_":
                completer = TermCompleter(['values('])
            elif state == "insert_into_x_values":
                completer = TermCompleter(['('])
            elif state == "insert_into_x_values(":
                completer = TermCompleter(["'"])

            elif state == "update_":
                completer = TermCompleter(self.tables())
            elif state == "update_x_":
                completer = TermCompleter(['set'])
            elif state in ["update_x_set_", "update_x_set_a=v,"]:
                completer = columns
            elif state == "update_x_set_a":
                completer = TermCompleter(['='])
            elif state == "update_x_set_a=":
                completer = TermCompleter(["'"])
            elif state == "update_x_set_a=v_":
                completer = TermCompleter(['where'])
            elif state == "update_x_set_a=v_where_":
                completer = columns
            elif state == "update_x_set_a=v_where_id":
                completer = TermCompleter(['='])
            elif state == "update_x_set_a=v_where_id=v_":
                completer = TermCompleter(['and', 'or'])

            elif state == "delete_":
                completer = TermCompleter(['from'])
            elif state == "delete_from_":
                completer = TermCompleter(self.tables())
            elif state == "delete_from_x_":
                completer = TermCompleter(['where'])
            elif state == "delete_from_x_where_":
                completer = columns
            elif state == "delete_from_x_where_id":
                completer = TermCompleter(['='])
            elif state == "delete_from_x_where_id=":
                completer = TermCompleter(["'"])
            elif state == "delete_from_x_where_id=v_":
                completer = TermCompleter(['and', 'or'])

        if completer:
            for c in completer.get_completions(document, complete_event):
                yield c

    def traverse_tokens(self, text: str, tokens: list[Token], state: str = None, indent=0):
        # state: str = None
        for token in tokens:
            if self.debug:
                if token.ttype == T.Whitespace:
                    print('_ ', end='')
                elif token.ttype in [T.DML, T.Wildcard, T.Punctuation]:
                    print(f'{token.value} ', end='')
                elif token.ttype:
                    tks = str(token.ttype).split('.')
                    typ = tks[len(tks) - 1]
                    if ' ' in token.value:
                        print(f'"{token.value}:{typ}" ', end='')
                    else:
                        print(f'{token.value}:{typ} ', end='')
                # print("  " * indent + f"Token: {token.value}, Type: {token.ttype}@{token.ttype.__class__}")
            node: str = None
            if token.is_group:
                state = self.traverse_tokens(text, token.tokens, state, indent + 1)
            else:
                if not state:
                    if token.ttype == T.Keyword.DML and token.value.lower() == 'select':
                        state = 'select'
                    if token.ttype == T.Keyword.DML and token.value.lower() == 'insert':
                        state = 'insert'
                    if token.ttype == T.Keyword.DML and token.value.lower() == 'update':
                        state = 'update'
                    if token.ttype == T.Keyword.DML and token.value.lower() == 'delete':
                        state = 'delete'
                    elif token.ttype == T.Name:
                        state = 'dml_incomplete'

                elif state == 'select':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_'
                elif state == 'select_':
                    if token.ttype == T.Name or token.ttype == T.Wildcard:
                        state = 'select_a'
                elif state == 'select_a':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_a_'
                    elif token.ttype == T.Punctuation and token.value == ',':
                        state = 'select_a,'
                elif state == 'select_a,':
                    if token.ttype == T.Name or token.ttype == T.Wildcard:
                        state = 'select_a'
                elif state == 'select_a_':
                    if token.ttype == T.Keyword and token.value.lower() == 'from':
                        state = 'select_a_from'
                elif state == 'select_a_from':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_a_from_'
                elif state == 'select_a_from_':
                    if token.ttype == T.Name:
                        state = 'select_a_from_x'
                elif state == 'select_a_from_x':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_a_from_x_'
                    elif token.ttype == T.Punctuation and token.value == ',':
                        state = 'select_a_from_x,'
                elif state == 'select_a_from_x,':
                    if token.ttype == T.Name:
                        state = 'select_a_from_x'
                elif state in ['select_a_from_x_', 'select_a_from_x_as_x_']:
                    if token.ttype == T.Punctuation and token.value == ',':
                        state = 'select_a_from_x,'
                    elif token.ttype == T.Keyword and token.value.lower() == 'as':
                        state = 'select_a_from_x_as'
                    elif token.ttype == T.Keyword and token.value.lower() == 'where':
                        state = 'select_a_from_x_where'
                    elif token.ttype == T.Keyword and token.value.lower() == 'limit':
                        state = 'select_a_from_x_where_id=v_limit'
                    elif token.ttype == T.Keyword and token.value.lower() == 'group':
                        state = 'select_a_from_x_group'
                    elif token.ttype == T.Keyword and token.value.lower() == 'group by':
                        state = 'select_a_from_x_group_by'
                    elif token.ttype == T.Keyword and token.value.lower() == 'inner':
                        state = 'select_a_from_x_inner'
                    elif token.ttype == T.Keyword and token.value.lower() == 'inner join':
                        state = 'select_a_from_x_inner_join'
                    elif token.ttype == T.Keyword and token.value.lower() == 'left':
                        state = 'select_a_from_x_left'
                    elif token.ttype == T.Keyword and token.value.lower() in ['left join', 'left outer join']:
                        state = 'select_a_from_x_inner_join'
                    elif token.ttype == T.Keyword and token.value.lower() == 'right':
                        state = 'select_a_from_x_right'
                    elif token.ttype == T.Keyword and token.value.lower() in ['right join', 'right outer join']:
                        state = 'select_a_from_x_inner_join'
                    elif token.ttype == T.Keyword and token.value.lower() == 'full':
                        state = 'select_a_from_x_full'
                    elif token.ttype == T.Keyword and token.value.lower() == 'full outer join':
                        state = 'select_a_from_x_inner_join'
                elif state == 'select_a_from_x_as':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_a_from_x_as_'
                elif state == 'select_a_from_x_as_':
                    if token.ttype == T.Name:
                        state = 'select_a_from_x_as_x'
                elif state == 'select_a_from_x_as_x':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_a_from_x_as_x_'
                    elif token.ttype == T.Punctuation and token.value == ',':
                        state = 'select_a_from_x_as_x,'
                elif state == 'select_a_from_x_as_x,':
                    if token.ttype == T.Name:
                        state = 'select_a_from_x'
                elif state == 'select_a_from_x_where':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_a_from_x_where_'
                elif state == 'select_a_from_x_where_':
                    if token.ttype == T.Name:
                        state = 'select_a_from_x_where_id'
                elif state == 'select_a_from_x_where_id':
                    if token.ttype == T.Operator.Comparison:
                        state = 'select_a_from_x_where_id='
                elif state == 'select_a_from_x_where_id=':
                    if token.ttype in [T.Literal.String.Single, T.Name]:
                        state = 'select_a_from_x_where_id=v'
                elif state == 'select_a_from_x_where_id=v':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_a_from_x_where_id=v_'
                elif state == 'select_a_from_x_where_id=v_':
                    if token.ttype == T.Keyword and token.value.lower() in ['and', 'or']:
                        state = 'select_a_from_x_where'
                    elif token.ttype == T.Keyword and token.value.lower() == 'group':
                        state = 'select_a_from_x_group'
                    elif token.ttype == T.Keyword and token.value.lower() == 'group by':
                        state = 'select_a_from_x_group_by'
                    elif token.ttype == T.Keyword and token.value.lower() == 'limit':
                        state = 'select_a_from_x_where_id=v_limit'
                elif state == 'select_a_from_x_group':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_a_from_x_group_'
                elif state == 'select_a_from_x_group_':
                    if token.ttype == T.Keyword and token.value.lower() == 'by':
                        state = 'select_a_from_x_group_by'
                elif state == 'select_a_from_x_group_by':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_a_from_x_group_by_'
                elif state == 'select_a_from_x_group_by_':
                    if token.ttype == T.Name:
                        state = 'select_a_from_x_group_by_a'
                elif state == 'select_a_from_x_group_by_a':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_a_from_x_group_by_a_'
                    elif token.ttype == T.Punctuation and token.value == ',':
                        state = 'select_a_from_x_group_by_a,'
                elif state == 'select_a_from_x_group_by_a,':
                    if token.ttype == T.Name:
                        state = 'select_a_from_x_group_by_a'
                elif state == 'select_a_from_x_group_by_a_':
                    if token.ttype == T.Keyword and token.value.lower() == 'limit':
                        state = 'select_a_from_x_where_id=v_limit'
                elif state == 'select_a_from_x_where_id=v_limit':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_a_from_x_where_id=v_limit_'
                elif state == 'select_a_from_x_inner':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_a_from_x_inner_'
                elif state == 'select_a_from_x_inner_':
                    if token.ttype == T.Keyword and token.value.lower() == 'join':
                        state = 'select_a_from_x_inner_join'
                elif state == 'select_a_from_x_inner_join':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_a_from_x_inner_join_'
                elif state == 'select_a_from_x_inner_join_':
                    if token.ttype == T.Name:
                        state = 'select_a_from_x_inner_join_y'

                elif state == 'select_a_from_x_left':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_a_from_x_left_'
                elif state == 'select_a_from_x_left_':
                    if token.ttype == T.Keyword and token.value.lower() == 'join':
                        state = 'select_a_from_x_inner_join'
                    elif token.ttype == T.Keyword and token.value.lower() == 'outer':
                        state = 'select_a_from_x_left_outer'
                elif state == 'select_a_from_x_left_outer':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_a_from_x_left_outer_'
                elif state == 'select_a_from_x_left_outer_':
                    if token.ttype == T.Keyword and token.value.lower() == 'join':
                        state = 'select_a_from_x_inner_join_'

                elif state == 'select_a_from_x_right':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_a_from_x_right_'
                elif state == 'select_a_from_x_right_':
                    if token.ttype == T.Keyword and token.value.lower() == 'join':
                        state = 'select_a_from_x_inner_join'
                    elif token.ttype == T.Keyword and token.value.lower() == 'outer':
                        state = 'select_a_from_x_right_outer'
                elif state == 'select_a_from_x_right_outer':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_a_from_x_right_outer_'
                elif state == 'select_a_from_x_right_outer_':
                    if token.ttype == T.Keyword and token.value.lower() == 'join':
                        state = 'select_a_from_x_inner_join_'

                elif state == 'select_a_from_x_full':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_a_from_x_full_'
                elif state == 'select_a_from_x_full_':
                    if token.ttype == T.Keyword and token.value.lower() == 'outer':
                        state = 'select_a_from_x_full_outer'
                elif state == 'select_a_from_x_full_outer':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_a_from_x_full_outer_'
                elif state == 'select_a_from_x_full_outer_':
                    if token.ttype == T.Keyword and token.value.lower() == 'join':
                        state = 'select_a_from_x_inner_join_'

                elif state == 'select_a_from_x_inner_join_y':
                    if token.ttype == T.Punctuation and token.value == ',':
                        state = 'select_a_from_x_inner_join_y,'
                    elif token.ttype == T.Text.Whitespace:
                        state = 'select_a_from_x_inner_join_y_'
                elif state == 'select_a_from_x_inner_join_y,':
                    if token.ttype == T.Name:
                        state = 'select_a_from_x_inner_join_y'
                elif state == 'select_a_from_x_inner_join_y_':
                    if token.ttype == T.Keyword and token.value.lower() == 'on':
                        state = 'select_a_from_x_inner_join_y_on'
                elif state == 'select_a_from_x_inner_join_y_on':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_a_from_x_inner_join_y_on_'
                elif state == 'select_a_from_x_inner_join_y_on_':
                    if token.ttype == T.Name:
                        state = 'select_a_from_x_inner_join_y_on_a'
                elif state == 'select_a_from_x_inner_join_y_on_a':
                    if token.ttype == T.Operator.Comparison:
                        state = 'select_a_from_x_inner_join_y_on_a='
                elif state == 'select_a_from_x_inner_join_y_on_a=':
                    if token.ttype in [T.Literal.String.Single, T.Name]:
                        state = 'select_a_from_x_inner_join_y_on_a=b'
                elif state == 'select_a_from_x_inner_join_y_on_a=b':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_a_from_x_inner_join_y_on_a=b_'
                    elif token.ttype == T.Punctuation and token.value == ',':
                        state = 'select_a_from_x_inner_join_y_on_'
                elif state == 'select_a_from_x_inner_join_y_on_a=b_':
                    if token.ttype == T.Keyword and token.value.lower() in ['and', 'or']:
                        state = 'select_a_from_x_inner_join'
                    elif token.ttype == T.Keyword and token.value.lower() == 'where':
                        state = 'select_a_from_x_where'
                    elif token.ttype == T.Keyword and token.value.lower() == 'group':
                        state = 'select_a_from_x_group'
                    elif token.ttype == T.Keyword and token.value.lower() == 'group by':
                        state = 'select_a_from_x_group_by'
                    elif token.ttype == T.Keyword and token.value.lower() == 'limit':
                        state = 'select_a_from_x_where_id=v_limit'

                elif state == 'insert':
                    if token.ttype == T.Text.Whitespace:
                        state = 'insert_'
                elif state == 'insert_':
                    if token.ttype == T.Keyword and token.value.lower() == 'into':
                        state = 'insert_into'
                elif state == 'insert_into':
                    if token.ttype == T.Text.Whitespace:
                        state = 'insert_into_'
                elif state == 'insert_into_':
                    if token.ttype == T.Name:
                        state = 'insert_into_x'
                elif state == 'insert_into_x':
                    if token.ttype == T.Text.Whitespace:
                        state = 'insert_into_x_'
                    elif token.ttype == T.Punctuation and token.value == '(':
                        state = 'insert_into_x('
                elif state == 'insert_into_x_':
                    if token.ttype == T.Punctuation and token.value == '(':
                        state = 'insert_into_x('
                    elif token.ttype == T.Keyword and token.value.lower() == 'values':
                        state = 'insert_into_x_values'
                elif state == 'insert_into_x(':
                    if token.ttype == T.Name:
                        state = 'insert_into_x(a'
                elif state == 'insert_into_x(a':
                    if token.ttype == T.Punctuation and token.value == ',':
                        state = 'insert_into_x(a,'
                    elif token.ttype == T.Punctuation and token.value == ')':
                        state = 'insert_into_x(a)'
                elif state == 'insert_into_x(a,':
                    if token.ttype == T.Name:
                        state = 'insert_into_x(a'
                elif state == 'insert_into_x(a)':
                    if token.ttype == T.Text.Whitespace:
                        state = 'insert_into_x(a)_'
                elif state == 'insert_into_x(a)_':
                    if token.ttype == T.Keyword and token.value.lower() == 'values':
                        state = 'insert_into_x_values'
                elif state == 'insert_into_x_values':
                    if token.ttype == T.Punctuation and token.value == '(':
                        state = 'insert_into_x_values('
                elif state == 'insert_into_x_values(':
                    if token.ttype in [T.Literal.String.Single, T.Name]:
                        state = 'insert_into_x_values(v'
                elif state == 'insert_into_x_values(v':
                    if token.ttype == T.Punctuation and token.value == ',':
                        state = 'insert_into_x_values(v,'
                    elif token.ttype == T.Punctuation and token.value == ')':
                        state = 'insert_into_x_values(v)'
                elif state == 'insert_into_x_values(v,':
                    if token.ttype in [T.Literal.String.Single, T.Name]:
                        state = 'insert_into_x_values(v'

                elif state == 'update':
                    if token.ttype == T.Text.Whitespace:
                        state = 'update_'
                elif state == 'update_':
                    if token.ttype == T.Name:
                        state = 'update_x'
                elif state == 'update_x':
                    if token.ttype == T.Text.Whitespace:
                        state = 'update_x_'
                elif state == 'update_x_':
                    if token.ttype == T.Keyword and token.value.lower() == 'set':
                        state = 'update_x_set'
                elif state == 'update_x_set':
                    if token.ttype == T.Text.Whitespace:
                        state = 'update_x_set_'
                elif state == 'update_x_set_':
                    if token.ttype == T.Name:
                        state = 'update_x_set_a'
                elif state == 'update_x_set_a':
                    if token.ttype == T.Operator.Comparison:
                        state = 'update_x_set_a='
                elif state == 'update_x_set_a=':
                    if token.ttype in [T.Literal.String.Single, T.Name]:
                        state = 'update_x_set_a=v'
                elif state == 'update_x_set_a=v':
                    if token.ttype == T.Punctuation and token.value == ',':
                        state = 'update_x_set_a=v,'
                    elif token.ttype == T.Text.Whitespace:
                        state = 'update_x_set_a=v_'
                elif state == 'update_x_set_a=v,':
                    if token.ttype == T.Name:
                        state = 'update_x_set_a'
                elif state == 'update_x_set_a=v_':
                    if token.ttype == T.Punctuation and token.value == ',':
                        state = 'update_x_set_a=v,'
                    elif token.ttype == T.Keyword and token.value.lower() == 'where':
                        state = 'update_x_set_a=v_where'
                elif state == 'update_x_set_a=v_where':
                    if token.ttype == T.Text.Whitespace:
                        state = 'update_x_set_a=v_where_'
                elif state == 'update_x_set_a=v_where_':
                    if token.ttype == T.Name:
                        state = 'update_x_set_a=v_where_id'
                elif state == 'update_x_set_a=v_where_id':
                    if token.ttype == T.Operator.Comparison:
                        state = 'update_x_set_a=v_where_id='
                elif state == 'update_x_set_a=v_where_id=':
                    if token.ttype in [T.Literal.String.Single, T.Name]:
                        state = 'update_x_set_a=v_where_id=v'
                elif state == 'update_x_set_a=v_where_id=v':
                    if token.ttype == T.Text.Whitespace:
                        state = 'update_x_set_a=v_where_id=v_'
                elif state == 'update_x_set_a=v_where_id=v_':
                    if token.ttype == T.Keyword and token.value.lower() in ['and', 'or']:
                        state = 'update_x_set_a=v_where'

                elif state == 'delete':
                    if token.ttype == T.Text.Whitespace:
                        state = 'delete_'
                elif state == 'delete_':
                    if token.ttype == T.Keyword and token.value.lower() == 'from':
                        state = 'delete_from'
                elif state == 'delete_from':
                    if token.ttype == T.Text.Whitespace:
                        state = 'delete_from_'
                elif state == 'delete_from_':
                    if token.ttype == T.Name:
                        state = 'delete_from_x'
                elif state == 'delete_from_x':
                    if token.ttype == T.Text.Whitespace:
                        state = 'delete_from_x_'
                elif state == 'delete_from_x_':
                    if token.ttype == T.Keyword and token.value.lower() == 'where':
                        state = 'delete_from_x_where'
                elif state == 'delete_from_x_where':
                    if token.ttype == T.Text.Whitespace:
                        state = 'delete_from_x_where_'
                elif state == 'delete_from_x_where_':
                    if token.ttype == T.Name:
                        state = 'delete_from_x_where_id'
                elif state == 'delete_from_x_where_id':
                    if token.ttype == T.Operator.Comparison:
                        state = 'delete_from_x_where_id='
                elif state == 'delete_from_x_where_id=':
                    if token.ttype in [T.Literal.String.Single, T.Name]:
                        state = 'delete_from_x_where_id=v'
                elif state == 'delete_from_x_where_id=v':
                    if token.ttype == T.Text.Whitespace:
                        state = 'delete_from_x_where_id=v_'
                elif state == 'delete_from_x_where_id=v_':
                    if token.ttype == T.Keyword and token.value.lower() in ['and', 'or']:
                        state = 'delete_from_x_where'

        return state

    def completions(table_names: Callable[[], list[str]]):
        return {
            'delete': SqlCompleter(table_names, 'delete'),
            'insert': SqlCompleter(table_names, 'insert'),
            'select': SqlCompleter(table_names, 'select'),
            'update': SqlCompleter(table_names, 'update'),
        }
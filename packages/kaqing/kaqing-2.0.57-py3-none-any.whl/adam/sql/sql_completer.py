from typing import Callable, Iterable
from prompt_toolkit.completion import CompleteEvent, Completer, Completion
from prompt_toolkit.document import Document
import sqlparse
from sqlparse.sql import Statement, Token
from sqlparse import tokens as T

from adam.sql.term_completer import TermCompleter

columns = TermCompleter(['id', 'x.', 'y.', 'z.'])

class SqlCompleter(Completer):
    # <select_statement> ::= SELECT <select_list>
    #                      FROM <table_expression>
    #                      [WHERE <search_condition>]
    #                      [<group_by_clause>]
    #                      [<having_clause>]
    #                      [<order_by_clause>]
    #                      [<limit_clause>]

    # <search_condition> ::= <boolean_term>
    #                      | <search_condition> OR <boolean_term>

    # <boolean_term> ::= <boolean_factor>
    #                  | <boolean_term> AND <boolean_factor>

    # <boolean_factor> ::= [NOT] <predicate>
    #                    | ([NOT] <search_condition>)

    # <predicate> ::= <comparison_predicate>
    #               | <between_predicate>
    #               | <in_predicate>
    #               | <like_predicate>
    #               | <null_predicate>
    #               | <exists_predicate>
    #               | <quantified_predicate>
    #               | <unique_predicate>
    #               | <match_predicate>
    #               | <overlaps_predicate>
    #               | <distinct_predicate>
    #               | <member_predicate>
    #               | <submultiset_predicate>
    #               | <set_predicate>

    # <comparison_predicate> ::= <row_value_expression> <comparison_operator> <row_value_expression>
    # <comparison_operator> ::= '=' | '<>' | '<' | '<=' | '>' | '>='

    # <row_value_expression> ::= <value_expression>
    #                          | (<value_expression> [ { <comma> <value_expression> }... ])

    # <value_expression> ::= <numeric_value_expression>
    #                      | <string_value_expression>
    #                      | <datetime_value_expression>
    #                      | <interval_value_expression>
    #                      | <boolean_value_expression>
    #                      | <user_defined_type_value_expression>
    #                      | <reference_value_expression>
    #                      | <collection_value_expression>
    #                      | <row_value_constructor>
    #                      | <case_expression>
    #                      | <cast_expression>
    #                      | <subquery>
    #                      | NULL
    #                      | DEFAULT
    #                      | <identifier>
    #                      | <literal>

    # <insert_statement> ::= INSERT INTO <table_name> [ ( <column_list> ) ]
    #                        VALUES ( <value_list> )
    #                      | INSERT INTO <table_name> [ ( <column_list> ) ]
    #                        <query_expression>

    # <table_name> ::= <identifier>

    # <column_list> ::= <column_name> [ , <column_list> ]

    # <column_name> ::= <identifier>

    # <value_list> ::= <expression> [ , <value_list> ]

    # <query_expression> ::= SELECT <select_list> FROM <table_reference_list> [ WHERE <search_condition> ] [ GROUP BY <grouping_column_list> ] [ HAVING <search_condition> ] [ ORDER BY <sort_specification_list> ]

    # <update_statement> ::= UPDATE <table_name>
    #                        SET <set_clause_list>
    #                        [WHERE <search_condition>]

    # <set_clause_list> ::= <set_clause> { , <set_clause> }

    # <set_clause> ::= <column_name> = <update_value>

    # <update_value> ::= <expression> | NULL | DEFAULT

    # <search_condition> ::= <boolean_expression>

    # <delete_statement> ::= DELETE FROM <table_name> [ WHERE <search_condition> ]

    # <table_name> ::= <identifier>

    # <search_condition> ::= <boolean_expression>

    # <boolean_expression> ::= <predicate>
    #                      | <boolean_expression> AND <predicate>
    #                      | <boolean_expression> OR <predicate>
    #                      | NOT <predicate>
    #                      | ( <boolean_expression> )

    # <predicate> ::= <expression> <comparison_operator> <expression>
    #              | <expression> IS NULL
    #              | <expression> IS NOT NULL
    #              | <expression> LIKE <pattern> [ ESCAPE <escape_character> ]
    #              | <expression> IN ( <expression_list> )
    #              | EXISTS ( <select_statement> )
    #              | ... (other predicates)

    # <comparison_operator> ::= = | <> | != | > | < | >= | <=

    # <expression> ::= <literal>
    #               | <column_name>
    #               | <function_call>
    #               | ( <expression> )
    #               | <expression> <arithmetic_operator> <expression>
    #               | ... (other expressions)

    # <literal> ::= <numeric_literal> | <string_literal> | <boolean_literal> | <date_literal> | ...

    # <column_name> ::= <identifier>

    # <identifier> ::= <letter> { <letter> | <digit> | _ }...

    # <pattern> ::= <string_literal>

    # <escape_character> ::= <string_literal> (single character)

    # <expression_list> ::= <expression> { , <expression> }...
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
            elif state == "select_from_":
                completer = TermCompleter(self.tables())
            elif state == "select_from_x_":
                completer = TermCompleter(['as', 'where', 'inner', 'left', 'right', 'full', 'group', 'limit'])
            elif state == "select_from_x_as_x_":
                completer = TermCompleter(['where', 'inner', 'left', 'right', 'full', 'group', 'limit'])
            elif state == "select_from_x,":
                completer = TermCompleter(self.tables())
            elif state == "select_from_x_as_":
                completer = TermCompleter(['x', 'y', 'z'])
            elif state == "select_from_x_as_x,":
                completer = TermCompleter(self.tables())
            elif state == "select_where_":
                completer = columns
            elif state in ["select_where_a", "select_where_a_"]:
                completer = TermCompleter(['=', '<', '<=', '>', '>=', '<>', 'like', 'not'])
            elif state == "select_where_a_not_":
                completer = TermCompleter(['like', 'in'])
            elif state == "select_where_a_op":
                completer = TermCompleter(["'"])
            elif state == "select_where_sc_":
                completer = TermCompleter(['and', 'or', 'group', 'limit'])
            elif state == "select_where_sc_limit_":
                completer = TermCompleter(['1'])
            elif state == "select_from_x_group_":
                completer = TermCompleter(['by'])
            elif state == "select_from_x_group_by_":
                completer = columns
            elif state == "select_from_x_group_by_a,":
                completer = columns
            elif state == "select_from_x_group_by_a_":
                completer = TermCompleter(['limit'])
            elif state == "select_from_x_group_by_a_limit_":
                completer = TermCompleter(['1'])
            elif state == "select_from_x_inner_":
                completer = TermCompleter(['join'])
            elif state in ["select_join_", "select_from_x_left_join_"]:
                completer = TermCompleter(self.tables())
            elif state == "select_x_join_y,":
                completer = TermCompleter(self.tables())
            elif state == "select_x_join_y_":
                completer = TermCompleter(['on'])
            elif state == "select_x_join_y_on_":
                completer = columns
            elif state == "select_x_join_y_on_a":
                completer = TermCompleter(['='])
            elif state == "select_x_join_y_on_a_op":
                completer = columns
            elif state == "select_x_join_y_on_a_opb_":
                completer = TermCompleter(['where', 'group', 'limit'])
            elif state == "select_from_x_left_":
                completer = TermCompleter(['outer', 'join'])
            elif state == "select_from_x_left_outer_":
                completer = TermCompleter(['join'])
            elif state == "select_from_x_right_":
                completer = TermCompleter(['outer', 'join'])
            elif state == "select_from_x_right_outer_":
                completer = TermCompleter(['join'])
            elif state == "select_from_x_full_":
                completer = TermCompleter(['outer'])
            elif state == "select_from_x_full_outer_":
                completer = TermCompleter(['join'])

            elif state == "insert_":
                completer = TermCompleter(['into'])
            elif state == "insert_into_":
                completer = TermCompleter(self.tables())
            elif state == "insert_into_x_":
                completer = TermCompleter(['values(', 'select'])
            elif state == "insert_into_x_lp_":
                completer = columns
            elif state == "insert_into_x_lp_a,":
                completer = columns
            elif state == "insert_into_x_lp_a_rp_":
                completer = TermCompleter(['values(', 'select'])
            elif state == "insert_values":
                completer = TermCompleter(['('])
            elif state == "insert_values_lp_":
                completer = TermCompleter(["'"])

            elif state == "update_":
                completer = TermCompleter(self.tables())
            elif state == "update_x_":
                completer = TermCompleter(['set'])
            elif state in ["update_x_set_", "update_x_set_sc,"]:
                completer = columns
            elif state == "update_x_set_a":
                completer = TermCompleter(['='])
            elif state == "update_x_set_a_op":
                completer = TermCompleter(["'"])
            elif state == "update_x_set_sc_":
                completer = TermCompleter(['where'])
            elif state == "update_where_":
                completer = columns
            elif state == "update_where_a":
                completer = TermCompleter(['='])
            elif state == "update_where_sc_":
                completer = TermCompleter(['and', 'or'])

            elif state == "delete_":
                completer = TermCompleter(['from'])
            elif state == "delete_from_":
                completer = TermCompleter(self.tables())
            elif state == "delete_from_x_":
                completer = TermCompleter(['where'])
            elif state == "delete_where_":
                completer = columns
            elif state == "delete_where_a":
                completer = TermCompleter(['='])
            elif state == "delete_where_a_op":
                completer = TermCompleter(["'"])
            elif state == "delete_where_sc_":
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
                        state = 'select_from'
                elif state == 'select_from':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_from_'
                elif state == 'select_from_':
                    if token.ttype == T.Name:
                        state = 'select_from_x'
                elif state == 'select_from_x':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_from_x_'
                    elif token.ttype == T.Punctuation and token.value == ',':
                        state = 'select_from_x,'
                elif state == 'select_from_x,':
                    if token.ttype == T.Name:
                        state = 'select_from_x'
                elif state in ['select_from_x_', 'select_from_x_as_x_']:
                    if token.ttype == T.Punctuation and token.value == ',':
                        state = 'select_from_x,'
                    elif token.ttype == T.Keyword and token.value.lower() == 'as':
                        state = 'select_from_x_as'
                    elif token.ttype == T.Keyword and token.value.lower() == 'where':
                        state = 'select_where'
                    elif token.ttype == T.Keyword and token.value.lower() == 'limit':
                        state = 'select_where_sc_limit'
                    elif token.ttype == T.Keyword and token.value.lower() == 'group':
                        state = 'select_from_x_group'
                    elif token.ttype == T.Keyword and token.value.lower() == 'group by':
                        state = 'select_from_x_group_by'
                    elif token.ttype == T.Keyword and token.value.lower() == 'inner':
                        state = 'select_from_x_inner'
                    elif token.ttype == T.Keyword and token.value.lower() == 'inner join':
                        state = 'select_join'
                    elif token.ttype == T.Keyword and token.value.lower() == 'left':
                        state = 'select_from_x_left'
                    elif token.ttype == T.Keyword and token.value.lower() in ['left join', 'left outer join']:
                        state = 'select_join'
                    elif token.ttype == T.Keyword and token.value.lower() == 'right':
                        state = 'select_from_x_right'
                    elif token.ttype == T.Keyword and token.value.lower() in ['right join', 'right outer join']:
                        state = 'select_join'
                    elif token.ttype == T.Keyword and token.value.lower() == 'full':
                        state = 'select_from_x_full'
                    elif token.ttype == T.Keyword and token.value.lower() == 'full outer join':
                        state = 'select_join'
                elif state == 'select_from_x_as':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_from_x_as_'
                elif state == 'select_from_x_as_':
                    if token.ttype == T.Name:
                        state = 'select_from_x_as_x'
                elif state == 'select_from_x_as_x':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_from_x_as_x_'
                    elif token.ttype == T.Punctuation and token.value == ',':
                        state = 'select_from_x_as_x,'
                elif state == 'select_from_x_as_x,':
                    if token.ttype == T.Name:
                        state = 'select_from_x'
                elif state == 'select_where':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_where_'
                elif state == 'select_where_':
                    if token.ttype == T.Name:
                        state = 'select_where_a'
                elif state == 'select_where_a':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_where_a_'
                    elif token.ttype == T.Operator.Comparison:
                        state = 'select_where_a_op'
                elif state == 'select_where_a_':
                    if token.ttype == T.Operator.Comparison:
                        state = 'select_where_a_op'
                    elif token.ttype == T.Keyword and token.value.lower() == 'not':
                        state = 'select_where_a_not'
                elif state == 'select_where_a_not':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_where_a_not_'
                elif state == 'select_where_a_not_':
                    if token.ttype == T.Operator.Comparison:
                        state = 'select_where_a_not_op'
                elif state == 'select_where_a_not_op':
                    if token.ttype in [T.Literal.String.Single, T.Name]:
                        state = 'select_where_sc'
                elif state == 'select_where_a_op':
                    if token.ttype in [T.Literal.String.Single, T.Name]:
                        state = 'select_where_sc'
                elif state == 'select_where_sc':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_where_sc_'
                elif state == 'select_where_sc_':
                    if token.ttype == T.Keyword and token.value.lower() in ['and', 'or']:
                        state = 'select_where'
                    elif token.ttype == T.Keyword and token.value.lower() == 'group':
                        state = 'select_from_x_group'
                    elif token.ttype == T.Keyword and token.value.lower() == 'group by':
                        state = 'select_from_x_group_by'
                    elif token.ttype == T.Keyword and token.value.lower() == 'limit':
                        state = 'select_where_sc_limit'
                elif state == 'select_from_x_group':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_from_x_group_'
                elif state == 'select_from_x_group_':
                    if token.ttype == T.Keyword and token.value.lower() == 'by':
                        state = 'select_from_x_group_by'
                elif state == 'select_from_x_group_by':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_from_x_group_by_'
                elif state == 'select_from_x_group_by_':
                    if token.ttype == T.Name:
                        state = 'select_from_x_group_by_a'
                elif state == 'select_from_x_group_by_a':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_from_x_group_by_a_'
                    elif token.ttype == T.Punctuation and token.value == ',':
                        state = 'select_from_x_group_by_a,'
                elif state == 'select_from_x_group_by_a,':
                    if token.ttype == T.Name:
                        state = 'select_from_x_group_by_a'
                elif state == 'select_from_x_group_by_a_':
                    if token.ttype == T.Keyword and token.value.lower() == 'limit':
                        state = 'select_where_sc_limit'
                elif state == 'select_where_sc_limit':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_where_sc_limit_'
                elif state == 'select_from_x_inner':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_from_x_inner_'
                elif state == 'select_from_x_inner_':
                    if token.ttype == T.Keyword and token.value.lower() == 'join':
                        state = 'select_join'
                elif state == 'select_join':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_join_'
                elif state == 'select_join_':
                    if token.ttype == T.Name:
                        state = 'select_x_join_y'

                elif state == 'select_from_x_left':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_from_x_left_'
                elif state == 'select_from_x_left_':
                    if token.ttype == T.Keyword and token.value.lower() == 'join':
                        state = 'select_join'
                    elif token.ttype == T.Keyword and token.value.lower() == 'outer':
                        state = 'select_from_x_left_outer'
                elif state == 'select_from_x_left_outer':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_from_x_left_outer_'
                elif state == 'select_from_x_left_outer_':
                    if token.ttype == T.Keyword and token.value.lower() == 'join':
                        state = 'select_join_'

                elif state == 'select_from_x_right':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_from_x_right_'
                elif state == 'select_from_x_right_':
                    if token.ttype == T.Keyword and token.value.lower() == 'join':
                        state = 'select_join'
                    elif token.ttype == T.Keyword and token.value.lower() == 'outer':
                        state = 'select_from_x_right_outer'
                elif state == 'select_from_x_right_outer':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_from_x_right_outer_'
                elif state == 'select_from_x_right_outer_':
                    if token.ttype == T.Keyword and token.value.lower() == 'join':
                        state = 'select_join_'

                elif state == 'select_from_x_full':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_from_x_full_'
                elif state == 'select_from_x_full_':
                    if token.ttype == T.Keyword and token.value.lower() == 'outer':
                        state = 'select_from_x_full_outer'
                elif state == 'select_from_x_full_outer':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_from_x_full_outer_'
                elif state == 'select_from_x_full_outer_':
                    if token.ttype == T.Keyword and token.value.lower() == 'join':
                        state = 'select_join_'

                elif state == 'select_x_join_y':
                    if token.ttype == T.Punctuation and token.value == ',':
                        state = 'select_x_join_y,'
                    elif token.ttype == T.Text.Whitespace:
                        state = 'select_x_join_y_'
                elif state == 'select_x_join_y,':
                    if token.ttype == T.Name:
                        state = 'select_x_join_y'
                elif state == 'select_x_join_y_':
                    if token.ttype == T.Keyword and token.value.lower() == 'on':
                        state = 'select_x_join_y_on'
                elif state == 'select_x_join_y_on':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_x_join_y_on_'
                elif state == 'select_x_join_y_on_':
                    if token.ttype == T.Name:
                        state = 'select_x_join_y_on_a'
                elif state == 'select_x_join_y_on_a':
                    if token.ttype == T.Operator.Comparison:
                        state = 'select_x_join_y_on_a_op'
                elif state == 'select_x_join_y_on_a_op':
                    if token.ttype in [T.Literal.String.Single, T.Name]:
                        state = 'select_x_join_y_on_a_opb'
                elif state == 'select_x_join_y_on_a_opb':
                    if token.ttype == T.Text.Whitespace:
                        state = 'select_x_join_y_on_a_opb_'
                    elif token.ttype == T.Punctuation and token.value == ',':
                        state = 'select_x_join_y_on_'
                elif state == 'select_x_join_y_on_a_opb_':
                    if token.ttype == T.Keyword and token.value.lower() in ['and', 'or']:
                        state = 'select_join'
                    elif token.ttype == T.Keyword and token.value.lower() == 'where':
                        state = 'select_where'
                    elif token.ttype == T.Keyword and token.value.lower() == 'group':
                        state = 'select_from_x_group'
                    elif token.ttype == T.Keyword and token.value.lower() == 'group by':
                        state = 'select_from_x_group_by'
                    elif token.ttype == T.Keyword and token.value.lower() == 'limit':
                        state = 'select_where_sc_limit'

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
                        state = 'insert_into_x_lp_'
                elif state == 'insert_into_x_':
                    if token.ttype == T.Punctuation and token.value == '(':
                        state = 'insert_into_x_lp_'
                    elif token.ttype == T.Keyword and token.value.lower() == 'values':
                        state = 'insert_values'
                elif state == 'insert_into_x_lp_':
                    if token.ttype == T.Name:
                        state = 'insert_into_x_lp_a'
                elif state == 'insert_into_x_lp_a':
                    if token.ttype == T.Punctuation and token.value == ',':
                        state = 'insert_into_x_lp_a,'
                    elif token.ttype == T.Punctuation and token.value == ')':
                        state = 'insert_into_x_lp_a_rp'
                elif state == 'insert_into_x_lp_a,':
                    if token.ttype == T.Name:
                        state = 'insert_into_x_lp_a'
                elif state == 'insert_into_x_lp_a_rp':
                    if token.ttype == T.Text.Whitespace:
                        state = 'insert_into_x_lp_a_rp_'
                elif state == 'insert_into_x_lp_a_rp_':
                    if token.ttype == T.Keyword and token.value.lower() == 'values':
                        state = 'insert_values'
                    elif token.ttype == T.Keyword.DML and token.value.lower() == 'select':
                        state = 'select_'
                elif state == 'insert_values':
                    if token.ttype == T.Punctuation and token.value == '(':
                        state = 'insert_values_lp_'
                elif state == 'insert_values_lp_':
                    if token.ttype in [T.Literal.String.Single, T.Name]:
                        state = 'insert_values_lp_v'
                elif state == 'insert_values_lp_v':
                    if token.ttype == T.Punctuation and token.value == ',':
                        state = 'insert_values_lp_v,'
                elif state == 'insert_values_lp_v,':
                    if token.ttype in [T.Literal.String.Single, T.Name]:
                        state = 'insert_values_lp_v'

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
                        state = 'update_x_set_a_op'
                elif state == 'update_x_set_a_op':
                    if token.ttype in [T.Literal.String.Single, T.Name]:
                        state = 'update_x_set_sc'
                elif state == 'update_x_set_sc':
                    if token.ttype == T.Punctuation and token.value == ',':
                        state = 'update_x_set_sc,'
                    elif token.ttype == T.Text.Whitespace:
                        state = 'update_x_set_sc_'
                elif state == 'update_x_set_sc,':
                    if token.ttype == T.Name:
                        state = 'update_x_set_a'
                elif state == 'update_x_set_sc_':
                    if token.ttype == T.Punctuation and token.value == ',':
                        state = 'update_x_set_sc,'
                    elif token.ttype == T.Keyword and token.value.lower() == 'where':
                        state = 'update_where'
                elif state == 'update_where':
                    if token.ttype == T.Text.Whitespace:
                        state = 'update_where_'
                elif state == 'update_where_':
                    if token.ttype == T.Name:
                        state = 'update_where_a'
                elif state == 'update_where_a':
                    if token.ttype == T.Operator.Comparison:
                        state = 'update_where_a_op'
                elif state == 'update_where_a_op':
                    if token.ttype in [T.Literal.String.Single, T.Name]:
                        state = 'update_where_sc'
                elif state == 'update_where_sc':
                    if token.ttype == T.Text.Whitespace:
                        state = 'update_where_sc_'
                elif state == 'update_where_sc_':
                    if token.ttype == T.Keyword and token.value.lower() in ['and', 'or']:
                        state = 'update_where'

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
                        state = 'delete_where'
                elif state == 'delete_where':
                    if token.ttype == T.Text.Whitespace:
                        state = 'delete_where_'
                elif state == 'delete_where_':
                    if token.ttype == T.Name:
                        state = 'delete_where_a'
                elif state == 'delete_where_a':
                    if token.ttype == T.Operator.Comparison:
                        state = 'delete_where_a_op'
                elif state == 'delete_where_a_op':
                    if token.ttype in [T.Literal.String.Single, T.Name]:
                        state = 'delete_where_sc'
                elif state == 'delete_where_sc':
                    if token.ttype == T.Text.Whitespace:
                        state = 'delete_where_sc_'
                elif state == 'delete_where_sc_':
                    if token.ttype == T.Keyword and token.value.lower() in ['and', 'or']:
                        state = 'delete_where'

        return state

    def completions(table_names: Callable[[], list[str]]):
        return {
            'delete': SqlCompleter(table_names, 'delete'),
            'insert': SqlCompleter(table_names, 'insert'),
            'select': SqlCompleter(table_names, 'select'),
            'update': SqlCompleter(table_names, 'update'),
        }
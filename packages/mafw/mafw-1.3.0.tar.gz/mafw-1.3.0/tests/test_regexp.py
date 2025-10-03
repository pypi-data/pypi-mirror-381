#  Copyright 2025 European Union
#  Author: Bulgheroni Antonio (antonio.bulgheroni@ec.europa.eu)
#  SPDX-License-Identifier: EUPL-1.2
"""
Unit tests for regexp module.
"""

from mafw.tools.regexp import extract_protocol, normalize_sql_spaces


class TestExtractProtocol:
    """Test cases for extract_protocol function."""

    def test_extract_protocol_valid_urls(self):
        """Test extracting protocol from valid URLs."""
        # Common database protocols
        assert extract_protocol('postgresql://user:pass@host:5432/db') == 'postgresql'
        assert extract_protocol('mysql://user:pass@host:3306/db') == 'mysql'
        assert extract_protocol('sqlite:///path/to/database.db') == 'sqlite'
        assert extract_protocol('mongodb://user:pass@host:27017/db') == 'mongodb'

        # Web protocols
        assert extract_protocol('http://example.com') == 'http'
        assert extract_protocol('https://example.com') == 'https'
        assert extract_protocol('ftp://example.com') == 'ftp'

        # Protocols with numbers, hyphens, underscores, dots, and plus signs
        assert extract_protocol('redis+sentinel://host:port') == 'redis+sentinel'
        assert extract_protocol('mssql+pyodbc://server/database') == 'mssql+pyodbc'
        assert extract_protocol('oracle+cx_oracle://user:pass@host') == 'oracle+cx_oracle'
        assert extract_protocol('protocol_123://host') == 'protocol_123'
        assert extract_protocol('my-protocol://host') == 'my-protocol'
        assert extract_protocol('protocol.v2://host') == 'protocol.v2'

    def test_extract_protocol_edge_cases(self):
        """Test edge cases for protocol extraction."""
        # Single character protocol
        assert extract_protocol('a://host') == 'a'

        # Protocol with all allowed characters
        assert extract_protocol('abc123-_+.def://host') == 'abc123-_+.def'

        # Minimal valid URL
        assert extract_protocol('x://') == 'x'

    def test_extract_protocol_invalid_urls(self):
        """Test protocol extraction with invalid URLs."""
        # No protocol separator
        assert extract_protocol('postgresql') is None
        assert extract_protocol('example.com') is None

        # Invalid protocol characters
        assert extract_protocol('POSTGRESQL://host') is None  # uppercase
        assert extract_protocol('post@gres://host') is None  # @ symbol
        assert extract_protocol('post gres://host') is None  # space
        assert extract_protocol('post#gres://host') is None  # # symbol

        # Empty or whitespace
        assert extract_protocol('') is None
        assert extract_protocol('   ') is None

        # Only separator
        assert extract_protocol('://') is None
        assert extract_protocol('://host') is None

        # Protocol doesn't start at beginning
        assert extract_protocol('prefix postgresql://host') is None

    def test_extract_protocol_special_cases(self):
        """Test special cases and potential edge scenarios."""
        # Multiple :// in URL (should match first)
        assert extract_protocol('http://example.com://path') == 'http'

        # URL with port and complex path
        assert extract_protocol('postgresql://user:pass@localhost:5432/mydb?ssl=true') == 'postgresql'

        # Very long protocol name
        long_protocol = 'a' * 50
        assert extract_protocol(f'{long_protocol}://host') == long_protocol


class TestNormalizeSqlSpaces:
    """Test cases for normalize_sql_spaces function."""

    def test_normalize_multiple_spaces(self):
        """Test normalization of multiple consecutive spaces."""
        # Multiple spaces between words
        assert normalize_sql_spaces('SELECT  *  FROM  table') == 'SELECT * FROM table'
        assert normalize_sql_spaces('SELECT   *   FROM   table') == 'SELECT * FROM table'

        # Many consecutive spaces
        assert normalize_sql_spaces('SELECT          *          FROM          table') == 'SELECT * FROM table'

        # Mixed multiple spaces
        assert normalize_sql_spaces('SELECT  *   FROM    table  WHERE     id = 1') == 'SELECT * FROM table WHERE id = 1'

    def test_normalize_leading_trailing_spaces(self):
        """Test trimming of leading and trailing spaces."""
        # Leading spaces
        assert normalize_sql_spaces('  SELECT * FROM table') == 'SELECT * FROM table'
        assert normalize_sql_spaces('     SELECT * FROM table') == 'SELECT * FROM table'

        # Trailing spaces
        assert normalize_sql_spaces('SELECT * FROM table  ') == 'SELECT * FROM table'
        assert normalize_sql_spaces('SELECT * FROM table     ') == 'SELECT * FROM table'

        # Both leading and trailing
        assert normalize_sql_spaces('  SELECT * FROM table  ') == 'SELECT * FROM table'
        assert normalize_sql_spaces('    SELECT * FROM table    ') == 'SELECT * FROM table'

    def test_normalize_preserves_other_whitespace(self):
        """Test that other whitespace characters are preserved."""
        # Tabs should be preserved
        assert normalize_sql_spaces('SELECT\t*\tFROM\ttable') == 'SELECT\t*\tFROM\ttable'

        # Newlines should be preserved
        assert normalize_sql_spaces('SELECT *\nFROM table') == 'SELECT *\nFROM table'

        # Carriage returns should be preserved
        assert normalize_sql_spaces('SELECT *\rFROM table') == 'SELECT *\rFROM table'

        # Mixed whitespace with multiple spaces
        assert (
            normalize_sql_spaces('SELECT  *\nFROM   table\t\tWHERE  id = 1') == 'SELECT *\nFROM table\t\tWHERE id = 1'
        )

    def test_normalize_edge_cases(self):
        """Test edge cases for SQL space normalization."""
        # Empty string
        assert normalize_sql_spaces('') == ''

        # Only spaces
        assert normalize_sql_spaces('   ') == ''
        assert normalize_sql_spaces('  ') == ''

        # Single space
        assert normalize_sql_spaces(' ') == ''

        # String with no spaces
        assert normalize_sql_spaces('SELECT*FROM*table') == 'SELECT*FROM*table'

        # Single word with leading/trailing spaces
        assert normalize_sql_spaces('  word  ') == 'word'

    def test_normalize_complex_sql_examples(self):
        """Test with realistic SQL query examples."""

        # INSERT statement
        sql_input = "INSERT   INTO   users   (name,  email)   VALUES   ('John',  'john@example.com')"
        expected = "INSERT INTO users (name, email) VALUES ('John', 'john@example.com')"
        assert normalize_sql_spaces(sql_input) == expected

        # UPDATE statement
        sql_input = "UPDATE   users   SET   name  =  'Jane'   WHERE   id  =  1  "
        expected = "UPDATE users SET name = 'Jane' WHERE id = 1"
        assert normalize_sql_spaces(sql_input) == expected

    def test_normalize_single_spaces_unchanged(self):
        """Test that strings with only single spaces remain unchanged."""
        # Already normalized strings
        assert normalize_sql_spaces('SELECT * FROM table') == 'SELECT * FROM table'
        assert (
            normalize_sql_spaces("INSERT INTO users (name) VALUES ('John')")
            == "INSERT INTO users (name) VALUES ('John')"
        )
        assert normalize_sql_spaces('a b c d e') == 'a b c d e'

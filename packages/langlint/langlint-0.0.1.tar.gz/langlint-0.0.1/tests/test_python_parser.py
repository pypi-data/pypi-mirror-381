"""
Python 解析器测试

测试 Python 解析器的各种功能，包括注释提取、文档字符串处理等。
"""

import pytest
from langlint.parsers.python_parser import PythonParser
from langlint.parsers.base import UnitType, ParseError


class TestPythonParser:
    """Python 解析器测试类"""
    
    def setup_method(self):
        """设置测试方法"""
        self.parser = PythonParser()
    
    def test_supported_extensions(self):
        """测试支持的扩展名"""
        extensions = self.parser.supported_extensions
        assert '.py' in extensions
        assert '.pyi' in extensions
        assert '.pyw' in extensions
    
    def test_supported_mime_types(self):
        """测试支持的 MIME 类型"""
        mime_types = self.parser.supported_mime_types
        assert 'text/x-python' in mime_types
        assert 'application/x-python-code' in mime_types
    
    def test_can_parse_python_file(self):
        """测试能否解析 Python 文件"""
        assert self.parser.can_parse('test.py')
        assert self.parser.can_parse('test.pyi')
        assert self.parser.can_parse('test.pyw')
        assert not self.parser.can_parse('test.txt')
    
    def test_can_parse_python_content(self):
        """测试能否解析 Python 内容"""
        python_content = '''
def hello():
    """这是一个测试函数"""
    return "Hello, World!"
'''
        assert self.parser.can_parse('test.py', python_content)
        
        non_python_content = '''
This is not Python code.
It's just plain text.
'''
        assert not self.parser.can_parse('test.py', non_python_content)
    
    def test_extract_single_line_comments(self):
        """测试提取单行注释"""
        content = '''
# 这是一个单行注释
def hello():
    # 这是函数内的注释
    return "Hello, World!"
'''
        result = self.parser.extract_translatable_units(content, 'test.py')
        
        assert len(result.units) == 2
        assert result.units[0].content == "这是一个单行注释"
        assert result.units[0].unit_type == UnitType.COMMENT
        assert result.units[1].content == "这是函数内的注释"
        assert result.units[1].unit_type == UnitType.COMMENT
    
    def test_extract_docstrings(self):
        """测试提取文档字符串"""
        content = '''
def hello():
    """这是一个函数的文档字符串"""
    return "Hello, World!"

class TestClass:
    """这是一个类的文档字符串"""
    
    def method(self):
        """这是一个方法的文档字符串"""
        pass
'''
        result = self.parser.extract_translatable_units(content, 'test.py')
        
        assert len(result.units) == 3
        assert result.units[0].content == "这是一个函数的文档字符串"
        assert result.units[0].unit_type == UnitType.DOCSTRING
        assert result.units[1].content == "这是一个类的文档字符串"
        assert result.units[1].unit_type == UnitType.DOCSTRING
        assert result.units[2].content == "这是一个方法的文档字符串"
        assert result.units[2].unit_type == UnitType.DOCSTRING
    
    def test_extract_string_literals(self):
        """测试提取字符串字面量"""
        content = '''
def hello():
    message = "这是一个字符串字面量"
    return message
'''
        result = self.parser.extract_translatable_units(content, 'test.py')
        
        assert len(result.units) == 1
        assert result.units[0].content == "这是一个字符串字面量"
        assert result.units[0].unit_type == UnitType.STRING_LITERAL
    
    def test_extract_multiline_docstrings(self):
        """测试提取多行文档字符串"""
        content = '''
def complex_function():
    """
    这是一个复杂的函数
    
    它包含多行文档字符串
    用于详细说明函数的功能
    """
    pass
'''
        result = self.parser.extract_translatable_units(content, 'test.py')
        
        assert len(result.units) == 1
        assert "这是一个复杂的函数" in result.units[0].content
        assert result.units[0].unit_type == UnitType.DOCSTRING
    
    def test_ignore_code_patterns(self):
        """测试忽略代码模式"""
        content = '''
def hello():
    # 这是正常的注释
    import os  # 这是导入语句
    from sys import path  # 这是导入语句
    return "Hello, World!"
'''
        result = self.parser.extract_translatable_units(content, 'test.py')
        
        # 应该只提取正常的注释，忽略导入语句
        assert len(result.units) == 1
        assert result.units[0].content == "这是正常的注释"
    
    def test_handle_empty_content(self):
        """测试处理空内容"""
        content = ''
        result = self.parser.extract_translatable_units(content, 'test.py')
        
        assert len(result.units) == 0
        assert result.file_type == "python"
        assert result.line_count == 1
    
    def test_handle_whitespace_only_comments(self):
        """测试处理只有空白字符的注释"""
        content = '''
def hello():
    #    
    # 这是正常注释
    return "Hello, World!"
'''
        result = self.parser.extract_translatable_units(content, 'test.py')
        
        # 应该只提取有内容的注释
        assert len(result.units) == 1
        assert result.units[0].content == "这是正常注释"
    
    def test_reconstruct_file(self):
        """测试重构文件"""
        original_content = '''
def hello():
    """原始文档字符串"""
    # 原始注释
    return "Hello, World!"
'''
        
        # 创建翻译后的单元
        translated_units = [
            self.parser._create_translatable_unit(
                self.parser._tokenize_content(original_content)[0],
                original_content
            )
        ]
        if translated_units[0]:
            translated_units[0].content = "Translated docstring"
        
        reconstructed = self.parser.reconstruct_file(
            original_content,
            translated_units,
            'test.py'
        )
        
        assert "Translated docstring" in reconstructed
    
    def test_parse_error_handling(self):
        """测试解析错误处理"""
        # 测试无效的 Python 代码
        invalid_content = '''
def hello(
    # 未闭合的函数定义
    return "Hello, World!"
'''
        
        with pytest.raises(ParseError):
            self.parser.extract_translatable_units(invalid_content, 'test.py')
    
    def test_metadata_information(self):
        """测试元数据信息"""
        content = '''
def hello():
    """文档字符串"""
    # 注释
    pass
'''
        result = self.parser.extract_translatable_units(content, 'test.py')
        
        assert result.metadata is not None
        assert result.metadata['parser'] == 'PythonParser'
        assert result.metadata['version'] == '1.0.0'
    
    def test_line_and_column_numbers(self):
        """测试行号和列号"""
        content = '''
def hello():
    """文档字符串"""
    # 注释
    pass
'''
        result = self.parser.extract_translatable_units(content, 'test.py')
        
        for unit in result.units:
            assert unit.line_number > 0
            assert unit.column_number > 0
    
    def test_context_information(self):
        """测试上下文信息"""
        content = '''
def hello():
    """文档字符串"""
    # 注释
    pass
'''
        result = self.parser.extract_translatable_units(content, 'test.py')
        
        for unit in result.units:
            assert unit.context is not None
            assert len(unit.context) > 0











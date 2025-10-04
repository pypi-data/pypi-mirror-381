"""
Markdown 解析器测试

测试 Markdown 解析器的各种功能，包括文本节点提取、结构保持等。
"""

import pytest
from langlint.parsers.markdown_parser import MarkdownParser
from langlint.parsers.base import UnitType, ParseError


class TestMarkdownParser:
    """Markdown 解析器测试类"""
    
    def setup_method(self):
        """设置测试方法"""
        self.parser = MarkdownParser()
    
    def test_supported_extensions(self):
        """测试支持的扩展名"""
        extensions = self.parser.supported_extensions
        assert '.md' in extensions
        assert '.markdown' in extensions
        assert '.mdown' in extensions
        assert '.mkd' in extensions
        assert '.mkdn' in extensions
    
    def test_supported_mime_types(self):
        """测试支持的 MIME 类型"""
        mime_types = self.parser.supported_mime_types
        assert 'text/markdown' in mime_types
        assert 'text/x-markdown' in mime_types
        assert 'application/markdown' in mime_types
    
    def test_can_parse_markdown_file(self):
        """测试能否解析 Markdown 文件"""
        assert self.parser.can_parse('test.md')
        assert self.parser.can_parse('test.markdown')
        assert not self.parser.can_parse('test.txt')
    
    def test_can_parse_markdown_content(self):
        """测试能否解析 Markdown 内容"""
        markdown_content = '''
# 标题

这是一个段落。

## 子标题

- 列表项1
- 列表项2
'''
        assert self.parser.can_parse('test.md', markdown_content)
        
        non_markdown_content = '''
This is not markdown.
It's just plain text.
'''
        assert not self.parser.can_parse('test.md', non_markdown_content)
    
    def test_extract_headings(self):
        """测试提取标题"""
        content = '''
# 主标题
## 子标题
### 三级标题
'''
        result = self.parser.extract_translatable_units(content, 'test.md')
        
        assert len(result.units) == 3
        assert result.units[0].content == "主标题"
        assert result.units[0].unit_type == UnitType.TEXT_NODE
        assert result.units[1].content == "子标题"
        assert result.units[1].unit_type == UnitType.TEXT_NODE
        assert result.units[2].content == "三级标题"
        assert result.units[2].unit_type == UnitType.TEXT_NODE
    
    def test_extract_paragraphs(self):
        """测试提取段落"""
        content = '''
这是一个段落。

这是另一个段落。
'''
        result = self.parser.extract_translatable_units(content, 'test.md')
        
        assert len(result.units) == 2
        assert result.units[0].content == "这是一个段落。"
        assert result.units[0].unit_type == UnitType.TEXT_NODE
        assert result.units[1].content == "这是另一个段落。"
        assert result.units[1].unit_type == UnitType.TEXT_NODE
    
    def test_extract_lists(self):
        """测试提取列表"""
        content = '''
- 列表项1
- 列表项2
- 列表项3

1. 有序列表项1
2. 有序列表项2
'''
        result = self.parser.extract_translatable_units(content, 'test.md')
        
        assert len(result.units) == 5
        for unit in result.units:
            assert unit.unit_type == UnitType.TEXT_NODE
    
    def test_extract_blockquotes(self):
        """测试提取引用块"""
        content = '''
> 这是一个引用块
> 包含多行内容
'''
        result = self.parser.extract_translatable_units(content, 'test.md')
        
        assert len(result.units) == 1
        assert "这是一个引用块" in result.units[0].content
        assert result.units[0].unit_type == UnitType.TEXT_NODE
    
    def test_ignore_code_blocks(self):
        """测试忽略代码块"""
        content = '''
这是一个段落。

```python
def hello():
    print("Hello, World!")
```

这是另一个段落。
'''
        result = self.parser.extract_translatable_units(content, 'test.md')
        
        # 应该只提取段落，忽略代码块
        assert len(result.units) == 2
        assert result.units[0].content == "这是一个段落。"
        assert result.units[1].content == "这是另一个段落。"
    
    def test_ignore_inline_code(self):
        """测试忽略行内代码"""
        content = '''
这是一个包含 `代码` 的段落。
'''
        result = self.parser.extract_translatable_units(content, 'test.md')
        
        # 应该提取段落但忽略行内代码
        assert len(result.units) == 1
        assert "这是一个包含" in result.units[0].content
        assert "的段落" in result.units[0].content
    
    def test_ignore_links(self):
        """测试忽略链接"""
        content = '''
这是一个包含 [链接](https://example.com) 的段落。
'''
        result = self.parser.extract_translatable_units(content, 'test.md')
        
        # 应该提取段落但忽略链接
        assert len(result.units) == 1
        assert "这是一个包含" in result.units[0].content
        assert "的段落" in result.units[0].content
    
    def test_ignore_images(self):
        """测试忽略图片"""
        content = '''
这是一个包含 ![图片](image.png) 的段落。
'''
        result = self.parser.extract_translatable_units(content, 'test.md')
        
        # 应该提取段落但忽略图片
        assert len(result.units) == 1
        assert "这是一个包含" in result.units[0].content
        assert "的段落" in result.units[0].content
    
    def test_extract_front_matter(self):
        """测试提取 Front Matter"""
        content = '''---
title: 文档标题
description: 文档描述
---

# 主标题

这是文档内容。
'''
        result = self.parser.extract_translatable_units(content, 'test.md')
        
        # 应该提取 Front Matter 和标题
        assert len(result.units) >= 2
        front_matter_units = [u for u in result.units if u.unit_type == UnitType.METADATA]
        assert len(front_matter_units) >= 2
    
    def test_handle_empty_content(self):
        """测试处理空内容"""
        content = ''
        result = self.parser.extract_translatable_units(content, 'test.md')
        
        assert len(result.units) == 0
        assert result.file_type == "markdown"
        assert result.line_count == 1
    
    def test_handle_whitespace_only_content(self):
        """测试处理只有空白字符的内容"""
        content = '''
    
    
    
'''
        result = self.parser.extract_translatable_units(content, 'test.md')
        
        # 应该不提取任何单元
        assert len(result.units) == 0
    
    def test_reconstruct_file(self):
        """测试重构文件"""
        original_content = '''
# 原始标题

这是原始段落。
'''
        
        # 创建翻译后的单元
        translated_units = [
            type('TranslatableUnit', (), {
                'content': 'Translated Title',
                'unit_type': UnitType.TEXT_NODE,
                'line_number': 2,
                'column_number': 1,
                'context': 'Markdown heading',
                'metadata': {'original_content': '# 原始标题'}
            })(),
            type('TranslatableUnit', (), {
                'content': 'This is translated paragraph.',
                'unit_type': UnitType.TEXT_NODE,
                'line_number': 4,
                'column_number': 1,
                'context': 'Markdown paragraph',
                'metadata': {'original_content': '这是原始段落。'}
            })()
        ]
        
        reconstructed = self.parser.reconstruct_file(
            original_content,
            translated_units,
            'test.md'
        )
        
        assert "Translated Title" in reconstructed
        assert "This is translated paragraph" in reconstructed
    
    def test_parse_error_handling(self):
        """测试解析错误处理"""
        # 测试无效的 Markdown 内容
        invalid_content = None
        
        with pytest.raises(ParseError):
            self.parser.extract_translatable_units(invalid_content, 'test.md')
    
    def test_metadata_information(self):
        """测试元数据信息"""
        content = '''
# 标题

段落内容
'''
        result = self.parser.extract_translatable_units(content, 'test.md')
        
        assert result.metadata is not None
        assert result.metadata['parser'] == 'MarkdownParser'
        assert result.metadata['version'] == '1.0.0'
    
    def test_line_and_column_numbers(self):
        """测试行号和列号"""
        content = '''
# 标题

段落内容
'''
        result = self.parser.extract_translatable_units(content, 'test.md')
        
        for unit in result.units:
            assert unit.line_number > 0
            assert unit.column_number > 0
    
    def test_context_information(self):
        """测试上下文信息"""
        content = '''
# 标题

段落内容
'''
        result = self.parser.extract_translatable_units(content, 'test.md')
        
        for unit in result.units:
            assert unit.context is not None
            assert len(unit.context) > 0
    
    def test_complex_markdown(self):
        """测试复杂 Markdown 内容"""
        content = '''
# 主标题

这是一个包含 **粗体** 和 *斜体* 的段落。

## 子标题

- 列表项1
- 列表项2
  - 嵌套列表项1
  - 嵌套列表项2

> 这是一个引用块
> 包含多行内容

```python
def hello():
    print("Hello, World!")
```

[链接](https://example.com) 和 ![图片](image.png)
'''
        result = self.parser.extract_translatable_units(content, 'test.md')
        
        # 应该提取标题、段落、列表项和引用块
        assert len(result.units) > 0
        
        # 检查是否忽略了代码块、链接和图片
        for unit in result.units:
            assert "def hello():" not in unit.content
            assert "https://example.com" not in unit.content
            assert "image.png" not in unit.content











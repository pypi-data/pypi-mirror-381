"""
端到端集成测试

测试 LangLint 的完整工作流程，从文件解析到翻译到重构。
"""

import pytest
import tempfile
import os
from pathlib import Path
from langlint.core import Dispatcher, Config
from langlint.translators.mock_translator import MockTranslator, MockConfig


class TestEndToEnd:
    """端到端测试类"""
    
    def setup_method(self):
        """设置测试方法"""
        self.config = Config()
        self.dispatcher = Dispatcher(self.config)
        self.translator = MockTranslator(MockConfig())
        
        # 创建临时目录
        self.temp_dir = tempfile.mkdtemp()
        self.temp_path = Path(self.temp_dir)
    
    def teardown_method(self):
        """清理测试方法"""
        import shutil
        shutil.rmtree(self.temp_dir)
    
    def test_python_file_workflow(self):
        """测试 Python 文件完整工作流程"""
        # 创建测试 Python 文件
        python_content = '''
"""
测试模块
包含中文注释和文档字符串
"""

def hello():
    """问候函数"""
    return "Hello, World!"

class TestClass:
    """测试类"""
    
    def method(self):
        """测试方法"""
        # 这是方法内的注释
        pass
'''
        
        test_file = self.temp_path / "test.py"
        test_file.write_text(python_content, encoding='utf-8')
        
        # 解析文件
        result = self.dispatcher.parse_file(str(test_file))
        
        # 验证解析结果
        assert len(result.units) > 0
        assert result.file_type == "python"
        
        # 翻译单元
        translated_units = []
        for unit in result.units:
            translated_unit = type('TranslatableUnit', (), {
                'content': f"[EN] {unit.content}",
                'unit_type': unit.unit_type,
                'line_number': unit.line_number,
                'column_number': unit.column_number,
                'context': unit.context,
                'metadata': unit.metadata
            })()
            translated_units.append(translated_unit)
        
        # 重构文件
        reconstructed = result.parser.reconstruct_file(
            python_content,
            translated_units,
            str(test_file)
        )
        
        # 验证重构结果
        assert "[EN]" in reconstructed
        assert "测试模块" not in reconstructed or "[EN]" in reconstructed
    
    def test_markdown_file_workflow(self):
        """测试 Markdown 文件完整工作流程"""
        # 创建测试 Markdown 文件
        markdown_content = '''
# 主标题

这是一个段落。

## 子标题

- 列表项1
- 列表项2

> 引用块内容
'''
        
        test_file = self.temp_path / "test.md"
        test_file.write_text(markdown_content, encoding='utf-8')
        
        # 解析文件
        result = self.dispatcher.parse_file(str(test_file))
        
        # 验证解析结果
        assert len(result.units) > 0
        assert result.file_type == "markdown"
        
        # 翻译单元
        translated_units = []
        for unit in result.units:
            translated_unit = type('TranslatableUnit', (), {
                'content': f"[EN] {unit.content}",
                'unit_type': unit.unit_type,
                'line_number': unit.line_number,
                'column_number': unit.column_number,
                'context': unit.context,
                'metadata': unit.metadata
            })()
            translated_units.append(translated_unit)
        
        # 重构文件
        reconstructed = result.parser.reconstruct_file(
            markdown_content,
            translated_units,
            str(test_file)
        )
        
        # 验证重构结果
        assert "[EN]" in reconstructed
    
    def test_notebook_file_workflow(self):
        """测试 Jupyter Notebook 文件完整工作流程"""
        # 创建测试 Notebook 文件
        notebook_content = {
            "cells": [
                {
                    "cell_type": "markdown",
                    "metadata": {},
                    "source": [
                        "# 测试 Notebook\n",
                        "\n",
                        "这是一个测试 Notebook。"
                    ]
                },
                {
                    "cell_type": "code",
                    "execution_count": None,
                    "metadata": {},
                    "outputs": [],
                    "source": [
                        "# 这是代码注释\n",
                        "print(\"Hello, World!\")"
                    ]
                }
            ],
            "metadata": {
                "kernelspec": {
                    "display_name": "Python 3",
                    "language": "python",
                    "name": "python3"
                }
            },
            "nbformat": 4,
            "nbformat_minor": 4
        }
        
        import json
        test_file = self.temp_path / "test.ipynb"
        test_file.write_text(json.dumps(notebook_content, indent=2), encoding='utf-8')
        
        # 解析文件
        result = self.dispatcher.parse_file(str(test_file))
        
        # 验证解析结果
        assert len(result.units) > 0
        assert result.file_type == "jupyter_notebook"
        
        # 翻译单元
        translated_units = []
        for unit in result.units:
            translated_unit = type('TranslatableUnit', (), {
                'content': f"[EN] {unit.content}",
                'unit_type': unit.unit_type,
                'line_number': unit.line_number,
                'column_number': unit.column_number,
                'context': unit.context,
                'metadata': unit.metadata
            })()
            translated_units.append(translated_unit)
        
        # 重构文件
        reconstructed = result.parser.reconstruct_file(
            json.dumps(notebook_content, indent=2),
            translated_units,
            str(test_file)
        )
        
        # 验证重构结果
        assert "[EN]" in reconstructed
    
    def test_multiple_file_types(self):
        """测试多种文件类型"""
        # 创建多种类型的测试文件
        files = {
            "test.py": '''
def hello():
    """问候函数"""
    return "Hello, World!"
''',
            "test.md": '''
# 标题

这是段落内容。
''',
            "test.js": '''
// 这是 JavaScript 注释
function hello() {
    return "Hello, World!";
}
'''
        }
        
        # 创建文件
        for filename, content in files.items():
            file_path = self.temp_path / filename
            file_path.write_text(content, encoding='utf-8')
        
        # 解析所有文件
        results = []
        for filename in files.keys():
            file_path = self.temp_path / filename
            result = self.dispatcher.parse_file(str(file_path))
            results.append(result)
        
        # 验证解析结果
        assert len(results) == 3
        for result in results:
            assert len(result.units) > 0
    
    def test_error_handling(self):
        """测试错误处理"""
        # 创建无效文件
        invalid_file = self.temp_path / "invalid.txt"
        invalid_file.write_text("This is not a supported file type.", encoding='utf-8')
        
        # 尝试解析无效文件
        result = self.dispatcher.parse_file(str(invalid_file))
        
        # 应该返回空结果或引发异常
        assert result is None or len(result.units) == 0
    
    def test_performance(self):
        """测试性能"""
        import time
        
        # 创建大量测试文件
        test_files = []
        for i in range(10):
            file_path = self.temp_path / f"test_{i}.py"
            content = f'''
def function_{i}():
    """函数 {i} 的文档字符串"""
    # 函数 {i} 的注释
    return {i}
'''
            file_path.write_text(content, encoding='utf-8')
            test_files.append(file_path)
        
        # 测量解析时间
        start_time = time.time()
        for file_path in test_files:
            result = self.dispatcher.parse_file(str(file_path))
            assert len(result.units) > 0
        end_time = time.time()
        
        # 验证性能（应该在合理时间内完成）
        duration = end_time - start_time
        assert duration < 10.0  # 应该在10秒内完成
    
    def test_memory_usage(self):
        """测试内存使用"""
        import psutil
        import gc
        
        # 记录初始内存使用
        initial_memory = psutil.Process().memory_info().rss
        
        # 创建大量测试文件
        test_files = []
        for i in range(100):
            file_path = self.temp_path / f"test_{i}.py"
            content = f'''
def function_{i}():
    """函数 {i} 的文档字符串"""
    # 函数 {i} 的注释
    return {i}
'''
            file_path.write_text(content, encoding='utf-8')
            test_files.append(file_path)
        
        # 解析所有文件
        for file_path in test_files:
            result = self.dispatcher.parse_file(str(file_path))
            assert len(result.units) > 0
        
        # 强制垃圾回收
        gc.collect()
        
        # 记录最终内存使用
        final_memory = psutil.Process().memory_info().rss
        memory_increase = final_memory - initial_memory
        
        # 验证内存使用（应该不会过度增长）
        assert memory_increase < 100 * 1024 * 1024  # 应该小于100MB











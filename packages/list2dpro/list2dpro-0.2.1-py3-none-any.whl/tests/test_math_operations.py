"""
List2DMath类单元测试
测试矩阵数学运算功能
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from list2dpro.math_operations import get_list_2d_math


def test_matrix_add():
    """测试矩阵加法"""
    math_ops = get_list_2d_math()
    
    # 正常情况测试
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    result = math_ops.matrix_add(matrix1, matrix2)
    expected = [[6, 8], [10, 12]]
    assert result == expected, f"矩阵加法错误: {result} != {expected}"
    print("✓ 矩阵加法测试通过")
    
    # 尺寸不匹配测试
    try:
        matrix3 = [[1, 2, 3]]
        math_ops.matrix_add(matrix1, matrix3)
        assert False, "应该抛出尺寸不匹配异常"
    except ValueError:
        print("✓ 尺寸不匹配异常测试通过")
    
    # 空矩阵测试
    result = math_ops.matrix_add([], [])
    assert result == [], "空矩阵测试失败"
    print("✓ 空矩阵测试通过")


def test_matrix_multiply():
    """测试矩阵乘法"""
    math_ops = get_list_2d_math()
    
    # 2x2矩阵乘法测试
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    result = math_ops.matrix_multiply(matrix1, matrix2)
    expected = [[19, 22], [43, 50]]
    assert result == expected, f"矩阵乘法错误: {result} != {expected}"
    print("✓ 2x2矩阵乘法测试通过")
    
    # 2x3和3x2矩阵乘法测试
    matrix3 = [[1, 2, 3], [4, 5, 6]]
    matrix4 = [[7, 8], [9, 10], [11, 12]]
    result = math_ops.matrix_multiply(matrix3, matrix4)
    expected = [[58, 64], [139, 154]]
    assert result == expected, f"矩阵乘法错误: {result} != {expected}"
    print("✓ 2x3和3x2矩阵乘法测试通过")


def test_scalar_multiply():
    """测试标量乘法"""
    math_ops = get_list_2d_math()
    
    matrix = [[1, 2], [3, 4]]
    result = math_ops.scalar_multiply(matrix, 2)
    expected = [[2, 4], [6, 8]]
    assert result == expected, f"标量乘法错误: {result} != {expected}"
    print("✓ 标量乘法测试通过")


def test_matrix_transpose():
    """测试矩阵转置"""
    math_ops = get_list_2d_math()
    
    matrix = [[1, 2, 3], [4, 5, 6]]
    result = math_ops.matrix_transpose(matrix)
    expected = [[1, 4], [2, 5], [3, 6]]
    assert result == expected, f"矩阵转置错误: {result} != {expected}"
    print("✓ 矩阵转置测试通过")


def test_matrix_determinant():
    """测试矩阵行列式"""
    math_ops = get_list_2d_math()
    
    # 2x2矩阵行列式
    matrix2x2 = [[1, 2], [3, 4]]
    result = math_ops.matrix_determinant(matrix2x2)
    expected = -2
    assert result == expected, f"2x2行列式错误: {result} != {expected}"
    print("✓ 2x2矩阵行列式测试通过")
    
    # 3x3矩阵行列式
    matrix3x3 = [[6, 1, 1], [4, -2, 5], [2, 8, 7]]
    result = math_ops.matrix_determinant(matrix3x3)
    expected = -306
    assert result == expected, f"3x3行列式错误: {result} != {expected}"
    print("✓ 3x3矩阵行列式测试通过")


def test_matrix_statistics():
    """测试矩阵统计函数"""
    math_ops = get_list_2d_math()
    
    matrix = [[1, 2, 3], [4, 5, 6]]
    
    # 测试总和
    total = math_ops.matrix_sum(matrix)
    assert total == 21, f"矩阵总和错误: {total} != 21"
    print("✓ 矩阵总和测试通过")
    
    # 测试平均值
    mean = math_ops.matrix_mean(matrix)
    assert mean == 3.5, f"矩阵平均值错误: {mean} != 3.5"
    print("✓ 矩阵平均值测试通过")
    
    # 测试最大值
    max_val = math_ops.matrix_max(matrix)
    assert max_val == 6, f"矩阵最大值错误: {max_val} != 6"
    print("✓ 矩阵最大值测试通过")
    
    # 测试最小值
    min_val = math_ops.matrix_min(matrix)
    assert min_val == 1, f"矩阵最小值错误: {min_val} != 1"
    print("✓ 矩阵最小值测试通过")


def test_apply_function():
    """测试应用函数"""
    math_ops = get_list_2d_math()
    
    matrix = [[1, 2], [3, 4]]
    
    # 应用平方函数
    result = math_ops.apply_function(matrix, lambda x: x ** 2)
    expected = [[1, 4], [9, 16]]
    assert result == expected, f"应用函数错误: {result} != {expected}"
    print("✓ 应用函数测试通过")


def test_normalize_matrix():
    """测试矩阵归一化"""
    math_ops = get_list_2d_math()
    
    matrix = [[1, 2], [3, 4]]
    
    # 最小-最大归一化
    result = math_ops.normalize_matrix(matrix, 'minmax')
    expected = [[0.0, 1/3], [2/3, 1.0]]
    
    # 由于浮点数精度问题，使用近似比较
    for i in range(len(result)):
        for j in range(len(result[0])):
            assert abs(result[i][j] - expected[i][j]) < 1e-10, f"归一化错误: {result} != {expected}"
    print("✓ 矩阵归一化测试通过")


def test_hadamard_product():
    """测试Hadamard积"""
    math_ops = get_list_2d_math()
    
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    result = math_ops.hadamard_product(matrix1, matrix2)
    expected = [[5, 12], [21, 32]]
    assert result == expected, f"Hadamard积错误: {result} != {expected}"
    print("✓ Hadamard积测试通过")


def test_matrix_concatenate():
    """测试矩阵拼接"""
    math_ops = get_list_2d_math()
    
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    
    # 垂直拼接
    result_vertical = math_ops.matrix_concatenate(matrix1, matrix2, 0)
    expected_vertical = [[1, 2], [3, 4], [5, 6], [7, 8]]
    assert result_vertical == expected_vertical, f"垂直拼接错误: {result_vertical} != {expected_vertical}"
    print("✓ 垂直拼接测试通过")
    
    # 水平拼接
    result_horizontal = math_ops.matrix_concatenate(matrix1, matrix2, 1)
    expected_horizontal = [[1, 2, 5, 6], [3, 4, 7, 8]]
    assert result_horizontal == expected_horizontal, f"水平拼接错误: {result_horizontal} != {expected_horizontal}"
    print("✓ 水平拼接测试通过")


def test_extract_submatrix():
    """测试提取子矩阵"""
    math_ops = get_list_2d_math()
    
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = math_ops.extract_submatrix(matrix, 0, 0, 1, 1)
    expected = [[1, 2], [4, 5]]
    assert result == expected, f"提取子矩阵错误: {result} != {expected}"
    print("✓ 提取子矩阵测试通过")


def run_all_tests():
    """运行所有测试"""
    print("开始运行List2DMath类单元测试...\n")
    
    try:
        test_matrix_add()
        test_matrix_multiply()
        test_scalar_multiply()
        test_matrix_transpose()
        test_matrix_determinant()
        test_matrix_statistics()
        test_apply_function()
        test_normalize_matrix()
        test_hadamard_product()
        test_matrix_concatenate()
        test_extract_submatrix()
        
        print("\n🎉 所有测试通过！")
        return True
        
    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        return False


if __name__ == "__main__":
    run_all_tests()
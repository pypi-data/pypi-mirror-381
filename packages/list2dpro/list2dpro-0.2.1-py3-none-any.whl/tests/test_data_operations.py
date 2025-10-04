"""
List2DData类单元测试
测试数据筛选转换功能
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from list2dpro.data_operations import get_list_2d_data


def test_filter_rows():
    """测试行筛选"""
    data_ops = get_list_2d_data()
    
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    # 筛选包含大于5的元素的行
    result = data_ops.filter_rows(matrix, lambda row: any(x > 5 for x in row))
    expected = [[4, 5, 6], [7, 8, 9]]
    assert result == expected, f"行筛选错误: {result} != {expected}"
    print("✓ 行筛选测试通过")


def test_filter_columns():
    """测试列筛选"""
    data_ops = get_list_2d_data()
    
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    # 筛选总和大于15的列（只有第3列满足条件）
    result = data_ops.filter_columns(matrix, lambda col: sum(col) > 15)
    expected = [[3], [6], [9]]
    assert result == expected, f"列筛选错误: {result} != {expected}"
    print("✓ 列筛选测试通过")


def test_filter_elements():
    """测试元素筛选"""
    data_ops = get_list_2d_data()
    
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    # 筛选大于5的元素
    result = data_ops.filter_elements(matrix, lambda x: x > 5)
    expected = [[None, None, None], [None, None, 6], [7, 8, 9]]
    assert result == expected, f"元素筛选错误: {result} != {expected}"
    print("✓ 元素筛选测试通过")


def test_sort_rows():
    """测试行排序"""
    data_ops = get_list_2d_data()
    
    matrix = [[3, 2, 1], [1, 2, 3], [2, 2, 2]]
    
    # 按第一列排序
    result = data_ops.sort_rows(matrix)
    expected = [[1, 2, 3], [2, 2, 2], [3, 2, 1]]
    assert result == expected, f"行排序错误: {result} != {expected}"
    print("✓ 行排序测试通过")


def test_sort_columns():
    """测试列排序"""
    data_ops = get_list_2d_data()
    
    matrix = [[3, 1, 2], [3, 1, 2], [3, 1, 2]]
    
    # 按第一行排序
    result = data_ops.sort_columns(matrix)
    expected = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    assert result == expected, f"列排序错误: {result} != {expected}"
    print("✓ 列排序测试通过")


def test_group_by_column():
    """测试按列分组"""
    data_ops = get_list_2d_data()
    
    matrix = [['A', 1, 10], ['B', 2, 20], ['A', 3, 30], ['B', 4, 40]]
    
    # 按第一列分组
    result = data_ops.group_by_column(matrix, 0)
    expected = {
        'A': [['A', 1, 10], ['A', 3, 30]],
        'B': [['B', 2, 20], ['B', 4, 40]]
    }
    assert result == expected, f"按列分组错误: {result} != {expected}"
    print("✓ 按列分组测试通过")


def test_unique_rows():
    """测试行去重"""
    data_ops = get_list_2d_data()
    
    matrix = [[1, 2, 3], [4, 5, 6], [1, 2, 3], [7, 8, 9]]
    
    result = data_ops.unique_rows(matrix)
    expected = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert result == expected, f"行去重错误: {result} != {expected}"
    print("✓ 行去重测试通过")


def test_map_rows():
    """测试行映射"""
    data_ops = get_list_2d_data()
    
    matrix = [[1, 2, 3], [4, 5, 6]]
    
    # 对每行元素加倍
    result = data_ops.map_rows(matrix, lambda row: [x * 2 for x in row])
    expected = [[2, 4, 6], [8, 10, 12]]
    assert result == expected, f"行映射错误: {result} != {expected}"
    print("✓ 行映射测试通过")


def test_map_columns():
    """测试列映射"""
    data_ops = get_list_2d_data()
    
    matrix = [[1, 2, 3], [4, 5, 6]]
    
    # 对每列求和，返回单元素列表
    result = data_ops.map_columns(matrix, lambda col: [sum(col)])
    expected = [[5, 7, 9]]  # 修正期望结果
    assert result == expected, f"列映射错误: {result} != {expected}"
    print("✓ 列映射测试通过")


def test_flatten_matrix():
    """测试矩阵展平"""
    data_ops = get_list_2d_data()
    
    matrix = [[1, 2, 3], [4, 5, 6]]
    
    result = data_ops.flatten_matrix(matrix)
    expected = [1, 2, 3, 4, 5, 6]
    assert result == expected, f"矩阵展平错误: {result} != {expected}"
    print("✓ 矩阵展平测试通过")


def test_reshape_matrix():
    """测试矩阵重塑"""
    data_ops = get_list_2d_data()
    
    matrix = [[1, 2, 3, 4, 5, 6]]
    
    result = data_ops.reshape_matrix(matrix, (2, 3))
    expected = [[1, 2, 3], [4, 5, 6]]
    assert result == expected, f"矩阵重塑错误: {result} != {expected}"
    print("✓ 矩阵重塑测试通过")


def test_find_all_matches():
    """测试查找匹配"""
    data_ops = get_list_2d_data()
    
    matrix = [['apple', 'banana'], ['cherry', 'date']]
    
    # 查找包含字母'a'的元素（apple, banana, date）
    result = data_ops.find_all_matches(matrix, 'a')
    expected = [(0, 0), (0, 1), (1, 1)]  # apple, banana, date
    assert result == expected, f"查找匹配错误: {result} != {expected}"
    print("✓ 查找匹配测试通过")


def test_replace_matches():
    """测试替换匹配"""
    data_ops = get_list_2d_data()
    
    matrix = [['apple', 'banana'], ['cherry', 'date']]
    
    # 替换包含字母'a'的元素为'fruit'
    result = data_ops.replace_matches(matrix, 'a', 'fruit')
    expected = [['fruit', 'fruit'], ['cherry', 'fruit']]
    assert result == expected, f"替换匹配错误: {result} != {expected}"
    print("✓ 替换匹配测试通过")


def test_pivot_table():
    """测试数据透视表"""
    data_ops = get_list_2d_data()
    
    matrix = [['A', 'X', 10], ['A', 'Y', 20], ['B', 'X', 30], ['B', 'Y', 40]]
    
    result = data_ops.pivot_table(matrix, 0, 1, 2, sum)
    expected = [
        ['', 'X', 'Y'],
        ['A', 10, 20],
        ['B', 30, 40]
    ]
    assert result == expected, f"数据透视表错误: {result} != {expected}"
    print("✓ 数据透视表测试通过")


def test_split_matrix():
    """测试矩阵分割"""
    data_ops = get_list_2d_data()
    
    matrix = [[1], [2], [3], [4], [5]]
    
    train, test = data_ops.split_matrix(matrix, 0.6)
    assert len(train) == 3, f"训练集大小错误: {len(train)} != 3"
    assert len(test) == 2, f"测试集大小错误: {len(test)} != 2"
    print("✓ 矩阵分割测试通过")


def test_shuffle_matrix():
    """测试矩阵打乱"""
    data_ops = get_list_2d_data()
    
    matrix = [[1], [2], [3], [4], [5]]
    
    result = data_ops.shuffle_matrix(matrix)
    # 检查是否包含相同的元素（顺序可能不同）
    assert len(result) == len(matrix), f"打乱后矩阵大小错误"
    assert set(tuple(row) for row in result) == set(tuple(row) for row in matrix), "打乱后元素不匹配"
    print("✓ 矩阵打乱测试通过")


def test_normalize_data_types():
    """测试数据类型标准化"""
    data_ops = get_list_2d_data()
    
    matrix = [['1', '2.5', 'hello'], ['3', '4.7', 'world']]
    
    result = data_ops.normalize_data_types(matrix)
    # 检查数字转换
    assert result[0][0] == 1, f"整数转换错误: {result[0][0]}"
    assert result[0][1] == 2.5, f"浮点数转换错误: {result[0][1]}"
    assert result[0][2] == 'hello', f"字符串保持错误: {result[0][2]}"
    print("✓ 数据类型标准化测试通过")


def test_remove_empty_rows():
    """测试移除空行"""
    data_ops = get_list_2d_data()
    
    matrix = [[1, 2, 3], [None, None, None], [4, 5, 6], ['', '', '']]
    
    result = data_ops.remove_empty_rows(matrix)
    expected = [[1, 2, 3], [4, 5, 6]]
    assert result == expected, f"移除空行错误: {result} != {expected}"
    print("✓ 移除空行测试通过")


def test_fill_missing_values():
    """测试填充缺失值"""
    data_ops = get_list_2d_data()
    
    matrix = [[1, None, 3], [4, '', 6]]
    
    result = data_ops.fill_missing_values(matrix, 0)
    expected = [[1, 0, 3], [4, 0, 6]]
    assert result == expected, f"填充缺失值错误: {result} != {expected}"
    print("✓ 填充缺失值测试通过")


def run_all_tests():
    """运行所有测试"""
    print("开始运行List2DData类单元测试...\n")
    
    try:
        test_filter_rows()
        test_filter_columns()
        test_filter_elements()
        test_sort_rows()
        test_sort_columns()
        test_group_by_column()
        test_unique_rows()
        test_map_rows()
        test_map_columns()
        test_flatten_matrix()
        test_reshape_matrix()
        test_find_all_matches()
        test_replace_matches()
        test_pivot_table()
        test_split_matrix()
        test_shuffle_matrix()
        test_normalize_data_types()
        test_remove_empty_rows()
        test_fill_missing_values()
        
        print("\n🎉 所有测试通过！")
        return True
        
    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        return False


if __name__ == "__main__":
    run_all_tests()
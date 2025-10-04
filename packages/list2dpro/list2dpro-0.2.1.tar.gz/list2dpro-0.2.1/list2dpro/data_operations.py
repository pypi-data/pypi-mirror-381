"""
数据筛选转换类
提供二维列表的数据筛选、过滤、转换和数据处理功能
"""

from typing import List, Any, Union, Optional, Callable, Tuple
import re


class List2DData:
    """
    二维列表数据操作类
    
    提供数据筛选、过滤、转换、排序、分组等数据处理功能
    专注于二维列表的数据处理操作
    """
    
    def __init__(self):
        """初始化数据操作类"""
        pass
    
    def filter_rows(self, matrix: List[List[Any]], 
                   condition: Callable[[List[Any]], bool]) -> List[List[Any]]:
        """
        根据条件筛选行
        
        Args:
            matrix: 输入矩阵
            condition: 筛选条件函数，接受一行数据返回布尔值
            
        Returns:
            满足条件的行组成的矩阵
        """
        try:
            if not matrix:
                print("Warning: 矩阵不能为空")
                return []
                
            result = []
            for row in matrix:
                if condition(row):
                    result.append(row.copy())
                    
            return result
            
        except Exception as e:
            print(f"Error in filter_rows: {e}")
            return []
    
    def filter_columns(self, matrix: List[List[Any]], 
                      condition: Callable[[List[Any]], bool]) -> List[List[Any]]:
        """
        根据条件筛选列
        
        Args:
            matrix: 输入矩阵
            condition: 筛选条件函数，接受一列数据返回布尔值
            
        Returns:
            满足条件的列组成的矩阵
        """
        try:
            if not matrix or not matrix[0]:
                print("Warning: 矩阵不能为空")
                return []
                
            # 转置矩阵以便按列处理
            transposed = list(map(list, zip(*matrix)))
            filtered_cols = []
            
            for col in transposed:
                if condition(col):
                    filtered_cols.append(col)
                    
            # 转置回原始格式
            if filtered_cols:
                result = list(map(list, zip(*filtered_cols)))
            else:
                result = []
                
            return result
            
        except Exception as e:
            print(f"Error in filter_columns: {e}")
            return []
    
    def filter_elements(self, matrix: List[List[Any]], 
                       condition: Callable[[Any], bool]) -> List[List[Any]]:
        """
        根据条件筛选元素
        
        Args:
            matrix: 输入矩阵
            condition: 筛选条件函数，接受单个元素返回布尔值
            
        Returns:
            满足条件的元素组成的矩阵（不满足条件的元素设为None）
        """
        try:
            if not matrix:
                print("Warning: 矩阵不能为空")
                return []
                
            result = []
            for row in matrix:
                new_row = []
                for element in row:
                    if condition(element):
                        new_row.append(element)
                    else:
                        new_row.append(None)
                result.append(new_row)
                
            return result
            
        except Exception as e:
            print(f"Error in filter_elements: {e}")
            return []
    
    def sort_rows(self, matrix: List[List[Any]], 
                 key: Optional[Callable[[List[Any]], Any]] = None, 
                 reverse: bool = False) -> List[List[Any]]:
        """
        按行排序矩阵
        
        Args:
            matrix: 输入矩阵
            key: 排序键函数，默认为按第一列排序
            reverse: 是否降序排序
            
        Returns:
            排序后的矩阵
        """
        try:
            if not matrix:
                print("Warning: 矩阵不能为空")
                return []
                
            if key is None:
                # 默认按第一列排序
                key = lambda row: row[0] if row else None
                
            # 创建行的副本进行排序
            sorted_matrix = sorted(matrix, key=key, reverse=reverse)
            return [row.copy() for row in sorted_matrix]
            
        except Exception as e:
            print(f"Error in sort_rows: {e}")
            return []
    
    def sort_columns(self, matrix: List[List[Any]], 
                   key: Optional[Callable[[List[Any]], Any]] = None, 
                   reverse: bool = False) -> List[List[Any]]:
        """
        按列排序矩阵
        
        Args:
            matrix: 输入矩阵
            key: 排序键函数，默认为按第一行排序
            reverse: 是否降序排序
            
        Returns:
            按列排序后的矩阵
        """
        try:
            if not matrix or not matrix[0]:
                print("Warning: 矩阵不能为空")
                return []
                
            # 转置矩阵进行排序
            transposed = list(map(list, zip(*matrix)))
            
            if key is None:
                # 默认按第一行排序
                key = lambda col: col[0] if col else None
                
            sorted_cols = sorted(transposed, key=key, reverse=reverse)
            
            # 转置回原始格式
            if sorted_cols:
                result = list(map(list, zip(*sorted_cols)))
            else:
                result = []
                
            return result
            
        except Exception as e:
            print(f"Error in sort_columns: {e}")
            return []
    
    def group_by_column(self, matrix: List[List[Any]], 
                       column_index: int) -> dict:
        """
        按指定列的值分组
        
        Args:
            matrix: 输入矩阵
            column_index: 用于分组的列索引
            
        Returns:
            分组字典，键为列值，值为对应的行列表
        """
        try:
            if not matrix or not matrix[0]:
                print("Warning: 矩阵不能为空")
                return {}
                
            if column_index < 0 or column_index >= len(matrix[0]):
                raise ValueError("列索引超出范围")
                
            groups = {}
            for row in matrix:
                key = row[column_index]
                if key not in groups:
                    groups[key] = []
                groups[key].append(row.copy())
                
            return groups
            
        except Exception as e:
            print(f"Error in group_by_column: {e}")
            return {}
    
    def unique_rows(self, matrix: List[List[Any]]) -> List[List[Any]]:
        """
        获取唯一的行（去重）
        
        Args:
            matrix: 输入矩阵
            
        Returns:
            去重后的矩阵
        """
        try:
            if not matrix:
                print("Warning: 矩阵不能为空")
                return []
                
            seen = set()
            result = []
            
            for row in matrix:
                # 将行转换为元组以便哈希
                row_tuple = tuple(row)
                if row_tuple not in seen:
                    seen.add(row_tuple)
                    result.append(row.copy())
                    
            return result
            
        except Exception as e:
            print(f"Error in unique_rows: {e}")
            return []
    
    def map_rows(self, matrix: List[List[Any]], 
                mapper: Callable[[List[Any]], List[Any]]) -> List[List[Any]]:
        """
        对每一行应用映射函数
        
        Args:
            matrix: 输入矩阵
            mapper: 映射函数，接受一行返回新的一行
            
        Returns:
            映射后的矩阵
        """
        try:
            if not matrix:
                print("Warning: 矩阵不能为空")
                return []
                
            result = []
            for row in matrix:
                try:
                    new_row = mapper(row)
                    result.append(new_row)
                except Exception as e:
                    print(f"Warning: 映射行时出错: {e}")
                    result.append(row.copy())
                    
            return result
            
        except Exception as e:
            print(f"Error in map_rows: {e}")
            return []
    
    def map_columns(self, matrix: List[List[Any]], 
                   mapper: Callable[[List[Any]], List[Any]]) -> List[List[Any]]:
        """
        对每一列应用映射函数
        
        Args:
            matrix: 输入矩阵
            mapper: 映射函数，接受一列返回新的一列
            
        Returns:
            映射后的矩阵
        """
        try:
            if not matrix or not matrix[0]:
                print("Warning: 矩阵不能为空")
                return []
                
            # 转置矩阵进行列映射
            transposed = list(map(list, zip(*matrix)))
            mapped_cols = []
            
            for col in transposed:
                try:
                    new_col = mapper(col)
                    # 确保新列是列表格式
                    if not isinstance(new_col, list):
                        new_col = [new_col]
                    mapped_cols.append(new_col)
                except Exception as e:
                    print(f"Warning: 映射列时出错: {e}")
                    mapped_cols.append(col.copy())
                    
            # 转置回原始格式
            if mapped_cols:
                # 确保所有列长度一致
                max_len = max(len(col) for col in mapped_cols)
                for col in mapped_cols:
                    if len(col) < max_len:
                        col.extend([None] * (max_len - len(col)))
                
                result = list(map(list, zip(*mapped_cols)))
            else:
                result = []
                
            return result
            
        except Exception as e:
            print(f"Error in map_columns: {e}")
            return []
    
    def flatten_matrix(self, matrix: List[List[Any]]) -> List[Any]:
        """
        将二维矩阵展平为一维列表
        
        Args:
            matrix: 输入矩阵
            
        Returns:
            展平后的一维列表
        """
        try:
            if not matrix:
                print("Warning: 矩阵不能为空")
                return []
                
            result = []
            for row in matrix:
                result.extend(row)
                
            return result
            
        except Exception as e:
            print(f"Error in flatten_matrix: {e}")
            return []
    
    def reshape_matrix(self, matrix: List[List[Any]], 
                      new_shape: Tuple[int, int]) -> List[List[Any]]:
        """
        重塑矩阵形状
        
        Args:
            matrix: 输入矩阵
            new_shape: 新形状 (行数, 列数)
            
        Returns:
            重塑后的矩阵
            
        Raises:
            ValueError: 如果新形状的元素数量不匹配
        """
        try:
            if not matrix:
                print("Warning: 矩阵不能为空")
                return []
                
            # 展平矩阵
            flat_list = self.flatten_matrix(matrix)
            rows, cols = new_shape
            
            # 检查元素数量是否匹配
            if len(flat_list) != rows * cols:
                raise ValueError(f"新形状({rows}x{cols})需要{rows*cols}个元素，但矩阵有{len(flat_list)}个元素")
                
            # 重塑为新的形状
            result = []
            for i in range(rows):
                start = i * cols
                end = start + cols
                result.append(flat_list[start:end])
                
            return result
            
        except Exception as e:
            print(f"Error in reshape_matrix: {e}")
            return []
    
    def find_all_matches(self, matrix: List[List[Any]], 
                        pattern: Union[str, Callable[[Any], bool]]) -> List[Tuple[int, int]]:
        """
        查找所有匹配指定模式的位置
        
        Args:
            matrix: 输入矩阵
            pattern: 匹配模式，可以是字符串（正则表达式）或函数
            
        Returns:
            匹配位置的列表 (行索引, 列索引)
        """
        try:
            if not matrix:
                print("Warning: 矩阵不能为空")
                return []
                
            matches = []
            
            for i, row in enumerate(matrix):
                for j, element in enumerate(row):
                    if isinstance(pattern, str):
                        # 使用正则表达式匹配（不区分大小写）
                        if re.search(pattern, str(element), re.IGNORECASE):
                            matches.append((i, j))
                    else:
                        # 使用函数匹配
                        if pattern(element):
                            matches.append((i, j))
                            
            return matches
            
        except Exception as e:
            print(f"Error in find_all_matches: {e}")
            return []
    
    def replace_matches(self, matrix: List[List[Any]], 
                       pattern: Union[str, Callable[[Any], bool]], 
                       replacement: Any) -> List[List[Any]]:
        """
        替换所有匹配指定模式的元素
        
        Args:
            matrix: 输入矩阵
            pattern: 匹配模式，可以是字符串（正则表达式）或函数
            replacement: 替换值
            
        Returns:
            替换后的矩阵
        """
        try:
            if not matrix:
                print("Warning: 矩阵不能为空")
                return []
                
            result = []
            for row in matrix:
                new_row = []
                for element in row:
                    if isinstance(pattern, str):
                        # 使用正则表达式匹配
                        if re.search(pattern, str(element)):
                            new_row.append(replacement)
                        else:
                            new_row.append(element)
                    else:
                        # 使用函数匹配
                        if pattern(element):
                            new_row.append(replacement)
                        else:
                            new_row.append(element)
                result.append(new_row)
                
            return result
            
        except Exception as e:
            print(f"Error in replace_matches: {e}")
            return []
    
    def pivot_table(self, matrix: List[List[Any]], 
                   row_index: int, 
                   col_index: int, 
                   value_index: int, 
                   agg_func: Callable[[List[Any]], Any] = sum) -> List[List[Any]]:
        """
        创建数据透视表
        
        Args:
            matrix: 输入矩阵
            row_index: 行索引列
            col_index: 列索引列
            value_index: 值列
            agg_func: 聚合函数，默认为求和
            
        Returns:
            数据透视表矩阵
        """
        try:
            if not matrix or not matrix[0]:
                print("Warning: 矩阵不能为空")
                return []
                
            # 获取唯一的行和列值
            row_values = sorted(set(row[row_index] for row in matrix))
            col_values = sorted(set(row[col_index] for row in matrix))
            
            # 创建透视表结构
            pivot_data = {}
            for row_val in row_values:
                pivot_data[row_val] = {col_val: [] for col_val in col_values}
            
            # 填充数据
            for row in matrix:
                row_val = row[row_index]
                col_val = row[col_index]
                value = row[value_index]
                pivot_data[row_val][col_val].append(value)
            
            # 创建结果矩阵
            result = []
            
            # 添加表头
            header = [""] + list(col_values)
            result.append(header)
            
            # 添加数据行
            for row_val in row_values:
                row_data = [row_val]
                for col_val in col_values:
                    values = pivot_data[row_val][col_val]
                    if values:
                        row_data.append(agg_func(values))
                    else:
                        row_data.append(None)
                result.append(row_data)
                
            return result
            
        except Exception as e:
            print(f"Error in pivot_table: {e}")
            return []
    
    def split_matrix(self, matrix: List[List[Any]], 
                    split_ratio: float = 0.8) -> Tuple[List[List[Any]], List[List[Any]]]:
        """
        分割矩阵为训练集和测试集
        
        Args:
            matrix: 输入矩阵
            split_ratio: 训练集比例 (0-1之间)
            
        Returns:
            (训练集矩阵, 测试集矩阵)
        """
        try:
            if not matrix:
                print("Warning: 矩阵不能为空")
                return [], []
                
            if split_ratio <= 0 or split_ratio >= 1:
                raise ValueError("分割比例必须在0和1之间")
                
            # 计算分割点
            split_index = int(len(matrix) * split_ratio)
            
            train_set = matrix[:split_index]
            test_set = matrix[split_index:]
            
            return train_set, test_set
            
        except Exception as e:
            print(f"Error in split_matrix: {e}")
            return [], []
    
    def shuffle_matrix(self, matrix: List[List[Any]]) -> List[List[Any]]:
        """
        随机打乱矩阵的行顺序
        
        Args:
            matrix: 输入矩阵
            
        Returns:
            打乱后的矩阵
        """
        try:
            if not matrix:
                print("Warning: 矩阵不能为空")
                return []
                
            import random
            shuffled = matrix.copy()
            random.shuffle(shuffled)
            return shuffled
            
        except Exception as e:
            print(f"Error in shuffle_matrix: {e}")
            return []
    
    def normalize_data_types(self, matrix: List[List[Any]]) -> List[List[Any]]:
        """
        尝试将矩阵中的数据类型标准化
        
        Args:
            matrix: 输入矩阵
            
        Returns:
            数据类型标准化后的矩阵
        """
        try:
            if not matrix:
                print("Warning: 矩阵不能为空")
                return []
                
            result = []
            for row in matrix:
                new_row = []
                for element in row:
                    # 尝试转换为适当的数据类型
                    if element is None:
                        new_row.append(None)
                    elif isinstance(element, (int, float)):
                        new_row.append(element)
                    else:
                        # 尝试转换为数字
                        try:
                            # 先尝试整数
                            int_val = int(element)
                            new_row.append(int_val)
                        except (ValueError, TypeError):
                            try:
                                # 再尝试浮点数
                                float_val = float(element)
                                new_row.append(float_val)
                            except (ValueError, TypeError):
                                # 保持原样
                                new_row.append(element)
                result.append(new_row)
                
            return result
            
        except Exception as e:
            print(f"Error in normalize_data_types: {e}")
            return []
    
    def remove_empty_rows(self, matrix: List[List[Any]]) -> List[List[Any]]:
        """
        移除空行（所有元素都为None或空字符串）
        
        Args:
            matrix: 输入矩阵
            
        Returns:
            移除空行后的矩阵
        """
        try:
            if not matrix:
                print("Warning: 矩阵不能为空")
                return []
                
            result = []
            for row in matrix:
                # 检查行是否为空
                is_empty = True
                for element in row:
                    if element is not None and element != "":
                        is_empty = False
                        break
                if not is_empty:
                    result.append(row.copy())
                    
            return result
            
        except Exception as e:
            print(f"Error in remove_empty_rows: {e}")
            return []
    
    def fill_missing_values(self, matrix: List[List[Any]], 
                          fill_value: Any = 0) -> List[List[Any]]:
        """
        填充缺失值（None或空字符串）
        
        Args:
            matrix: 输入矩阵
            fill_value: 填充值
            
        Returns:
            填充缺失值后的矩阵
        """
        try:
            if not matrix:
                print("Warning: 矩阵不能为空")
                return []
                
            result = []
            for row in matrix:
                new_row = []
                for element in row:
                    if element is None or element == "":
                        new_row.append(fill_value)
                    else:
                        new_row.append(element)
                result.append(new_row)
                
            return result
            
        except Exception as e:
            print(f"Error in fill_missing_values: {e}")
            return []


def get_list_2d_data():
    """获取List2DData实例"""
    return List2DData()
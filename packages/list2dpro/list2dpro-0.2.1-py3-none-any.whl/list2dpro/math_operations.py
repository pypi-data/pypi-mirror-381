"""
矩阵数学运算类
提供二维列表的数学运算功能，包括矩阵运算、统计计算等
"""

import math
from typing import List, Any, Union, Optional, Callable


class List2DMath:
    """
    二维列表数学运算类
    
    提供矩阵运算、统计计算、数学变换等功能
    继承自List2DEdit的基础操作，专注于数学运算
    """
    
    def __init__(self):
        """初始化数学运算类"""
        pass
    
    def matrix_add(self, matrix1: List[List[Union[int, float]]], 
                   matrix2: List[List[Union[int, float]]]) -> List[List[Union[int, float]]]:
        """
        矩阵加法运算
        
        Args:
            matrix1: 第一个矩阵
            matrix2: 第二个矩阵
            
        Returns:
            两个矩阵相加的结果矩阵
            
        Raises:
            ValueError: 如果矩阵尺寸不匹配
        """
        try:
            if not matrix1 or not matrix2:
                print("Warning: 矩阵不能为空")
                return []
                
            # 检查矩阵尺寸是否匹配
            if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
                raise ValueError("矩阵尺寸不匹配，无法进行加法运算")
                
            # 执行矩阵加法
            result = []
            for i in range(len(matrix1)):
                row = []
                for j in range(len(matrix1[0])):
                    # 确保元素是数字类型
                    try:
                        val1 = float(matrix1[i][j]) if matrix1[i][j] is not None else 0
                        val2 = float(matrix2[i][j]) if matrix2[i][j] is not None else 0
                        row.append(val1 + val2)
                    except (ValueError, TypeError):
                        print(f"Warning: 位置({i},{j})的元素无法转换为数字，使用0代替")
                        row.append(0)
                result.append(row)
                
            return result
            
        except ValueError as e:
            # 重新抛出尺寸不匹配异常
            raise e
        except Exception as e:
            print(f"Error in matrix_add: {e}")
            return []
    
    def matrix_multiply(self, matrix1: List[List[Union[int, float]]], 
                        matrix2: List[List[Union[int, float]]]) -> List[List[Union[int, float]]]:
        """
        矩阵乘法运算
        
        Args:
            matrix1: 第一个矩阵 (m x n)
            matrix2: 第二个矩阵 (n x p)
            
        Returns:
            矩阵相乘的结果矩阵 (m x p)
            
        Raises:
            ValueError: 如果矩阵尺寸不满足乘法条件
        """
        try:
            if not matrix1 or not matrix2:
                print("Warning: 矩阵不能为空")
                return []
                
            # 检查矩阵乘法条件：matrix1的列数等于matrix2的行数
            if len(matrix1[0]) != len(matrix2):
                raise ValueError("矩阵尺寸不满足乘法条件")
                
            # 初始化结果矩阵
            result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
            
            # 执行矩阵乘法
            for i in range(len(matrix1)):
                for j in range(len(matrix2[0])):
                    for k in range(len(matrix2)):
                        try:
                            val1 = float(matrix1[i][k]) if matrix1[i][k] is not None else 0
                            val2 = float(matrix2[k][j]) if matrix2[k][j] is not None else 0
                            result[i][j] += val1 * val2
                        except (ValueError, TypeError):
                            print(f"Warning: 位置({i},{k})或({k},{j})的元素无法转换为数字，跳过")
                            
            return result
            
        except Exception as e:
            print(f"Error in matrix_multiply: {e}")
            return []
    
    def scalar_multiply(self, matrix: List[List[Union[int, float]]], 
                       scalar: Union[int, float]) -> List[List[Union[int, float]]]:
        """
        矩阵标量乘法
        
        Args:
            matrix: 输入矩阵
            scalar: 标量值
            
        Returns:
            矩阵与标量相乘的结果
        """
        try:
            if not matrix:
                print("Warning: 矩阵不能为空")
                return []
                
            result = []
            for i in range(len(matrix)):
                row = []
                for j in range(len(matrix[0])):
                    try:
                        val = float(matrix[i][j]) if matrix[i][j] is not None else 0
                        row.append(val * scalar)
                    except (ValueError, TypeError):
                        print(f"Warning: 位置({i},{j})的元素无法转换为数字，使用0代替")
                        row.append(0)
                result.append(row)
                
            return result
            
        except Exception as e:
            print(f"Error in scalar_multiply: {e}")
            return []
    
    def matrix_transpose(self, matrix: List[List[Any]]) -> List[List[Any]]:
        """
        矩阵转置
        
        Args:
            matrix: 输入矩阵
            
        Returns:
            转置后的矩阵
        """
        try:
            if not matrix or not matrix[0]:
                print("Warning: 矩阵不能为空")
                return []
                
            # 使用zip进行转置
            transposed = list(map(list, zip(*matrix)))
            return transposed
            
        except Exception as e:
            print(f"Error in matrix_transpose: {e}")
            return []
    
    def matrix_determinant(self, matrix: List[List[Union[int, float]]]) -> float:
        """
        计算方阵的行列式（仅支持2x2和3x3矩阵）
        
        Args:
            matrix: 输入方阵
            
        Returns:
            矩阵的行列式值
            
        Raises:
            ValueError: 如果不是方阵或尺寸不支持
        """
        try:
            if not matrix or len(matrix) != len(matrix[0]):
                raise ValueError("输入必须是方阵")
                
            n = len(matrix)
            
            if n == 1:
                # 1x1矩阵的行列式就是元素本身
                return float(matrix[0][0]) if matrix[0][0] is not None else 0
            elif n == 2:
                # 2x2矩阵行列式: ad - bc
                a = float(matrix[0][0]) if matrix[0][0] is not None else 0
                b = float(matrix[0][1]) if matrix[0][1] is not None else 0
                c = float(matrix[1][0]) if matrix[1][0] is not None else 0
                d = float(matrix[1][1]) if matrix[1][1] is not None else 0
                return a * d - b * c
            elif n == 3:
                # 3x3矩阵行列式: a(ei - fh) - b(di - fg) + c(dh - eg)
                a = float(matrix[0][0]) if matrix[0][0] is not None else 0
                b = float(matrix[0][1]) if matrix[0][1] is not None else 0
                c = float(matrix[0][2]) if matrix[0][2] is not None else 0
                d = float(matrix[1][0]) if matrix[1][0] is not None else 0
                e = float(matrix[1][1]) if matrix[1][1] is not None else 0
                f = float(matrix[1][2]) if matrix[1][2] is not None else 0
                g = float(matrix[2][0]) if matrix[2][0] is not None else 0
                h = float(matrix[2][1]) if matrix[2][1] is not None else 0
                i = float(matrix[2][2]) if matrix[2][2] is not None else 0
                return a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)
            else:
                raise ValueError(f"不支持{n}x{n}矩阵的行列式计算")
                
        except Exception as e:
            print(f"Error in matrix_determinant: {e}")
            return 0.0
    
    def matrix_sum(self, matrix: List[List[Union[int, float]]]) -> float:
        """
        计算矩阵所有元素的和
        
        Args:
            matrix: 输入矩阵
            
        Returns:
            矩阵元素总和
        """
        try:
            if not matrix:
                print("Warning: 矩阵不能为空")
                return 0.0
                
            total = 0.0
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    try:
                        val = float(matrix[i][j]) if matrix[i][j] is not None else 0
                        total += val
                    except (ValueError, TypeError):
                        print(f"Warning: 位置({i},{j})的元素无法转换为数字，跳过")
                        
            return total
            
        except Exception as e:
            print(f"Error in matrix_sum: {e}")
            return 0.0
    
    def matrix_mean(self, matrix: List[List[Union[int, float]]]) -> float:
        """
        计算矩阵所有元素的平均值
        
        Args:
            matrix: 输入矩阵
            
        Returns:
            矩阵元素平均值
        """
        try:
            if not matrix or not matrix[0]:
                print("Warning: 矩阵不能为空")
                return 0.0
                
            total = self.matrix_sum(matrix)
            count = len(matrix) * len(matrix[0])
            return total / count if count > 0 else 0.0
            
        except Exception as e:
            print(f"Error in matrix_mean: {e}")
            return 0.0
    
    def matrix_max(self, matrix: List[List[Union[int, float]]]) -> float:
        """
        找出矩阵中的最大值
        
        Args:
            matrix: 输入矩阵
            
        Returns:
            矩阵中的最大值
        """
        try:
            if not matrix or not matrix[0]:
                print("Warning: 矩阵不能为空")
                return 0.0
                
            max_val = float('-inf')
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    try:
                        val = float(matrix[i][j]) if matrix[i][j] is not None else 0
                        if val > max_val:
                            max_val = val
                    except (ValueError, TypeError):
                        continue
                        
            return max_val if max_val != float('-inf') else 0.0
            
        except Exception as e:
            print(f"Error in matrix_max: {e}")
            return 0.0
    
    def matrix_min(self, matrix: List[List[Union[int, float]]]) -> float:
        """
        找出矩阵中的最小值
        
        Args:
            matrix: 输入矩阵
            
        Returns:
            矩阵中的最小值
        """
        try:
            if not matrix or not matrix[0]:
                print("Warning: 矩阵不能为空")
                return 0.0
                
            min_val = float('inf')
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    try:
                        val = float(matrix[i][j]) if matrix[i][j] is not None else 0
                        if val < min_val:
                            min_val = val
                    except (ValueError, TypeError):
                        continue
                        
            return min_val if min_val != float('inf') else 0.0
            
        except Exception as e:
            print(f"Error in matrix_min: {e}")
            return 0.0
    
    def apply_function(self, matrix: List[List[Any]], 
                      func: Callable[[Any], Any]) -> List[List[Any]]:
        """
        对矩阵中的每个元素应用函数
        
        Args:
            matrix: 输入矩阵
            func: 要应用的函数
            
        Returns:
            应用函数后的新矩阵
        """
        try:
            if not matrix:
                print("Warning: 矩阵不能为空")
                return []
                
            result = []
            for i in range(len(matrix)):
                row = []
                for j in range(len(matrix[0])):
                    try:
                        new_val = func(matrix[i][j])
                        row.append(new_val)
                    except Exception as e:
                        print(f"Warning: 对位置({i},{j})的元素应用函数失败: {e}")
                        row.append(matrix[i][j])
                result.append(row)
                
            return result
            
        except Exception as e:
            print(f"Error in apply_function: {e}")
            return []
    
    def normalize_matrix(self, matrix: List[List[Union[int, float]]], 
                        method: str = 'minmax') -> List[List[float]]:
        """
        矩阵归一化
        
        Args:
            matrix: 输入矩阵
            method: 归一化方法 ('minmax' 或 'zscore')
            
        Returns:
            归一化后的矩阵
        """
        try:
            if not matrix or not matrix[0]:
                print("Warning: 矩阵不能为空")
                return []
                
            if method == 'minmax':
                # 最小-最大归一化
                min_val = self.matrix_min(matrix)
                max_val = self.matrix_max(matrix)
                
                if max_val == min_val:
                    # 所有元素相同的情况
                    return [[0.5 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
                
                result = []
                for i in range(len(matrix)):
                    row = []
                    for j in range(len(matrix[0])):
                        try:
                            val = float(matrix[i][j]) if matrix[i][j] is not None else 0
                            normalized = (val - min_val) / (max_val - min_val)
                            row.append(normalized)
                        except (ValueError, TypeError):
                            row.append(0.0)
                    result.append(row)
                    
            elif method == 'zscore':
                # Z-score归一化
                mean_val = self.matrix_mean(matrix)
                # 计算标准差
                variance = 0.0
                count = 0
                for i in range(len(matrix)):
                    for j in range(len(matrix[0])):
                        try:
                            val = float(matrix[i][j]) if matrix[i][j] is not None else 0
                            variance += (val - mean_val) ** 2
                            count += 1
                        except (ValueError, TypeError):
                            continue
                
                std_dev = math.sqrt(variance / count) if count > 0 else 1.0
                
                result = []
                for i in range(len(matrix)):
                    row = []
                    for j in range(len(matrix[0])):
                        try:
                            val = float(matrix[i][j]) if matrix[i][j] is not None else 0
                            normalized = (val - mean_val) / std_dev
                            row.append(normalized)
                        except (ValueError, TypeError):
                            row.append(0.0)
                    result.append(row)
                    
            else:
                print("Warning: 不支持的归一化方法，使用minmax")
                return self.normalize_matrix(matrix, 'minmax')
                
            return result
            
        except Exception as e:
            print(f"Error in normalize_matrix: {e}")
            return []
    
    def matrix_power(self, matrix: List[List[Union[int, float]]], 
                    power: int) -> List[List[Union[int, float]]]:
        """
        矩阵的幂运算（仅支持方阵）
        
        Args:
            matrix: 输入方阵
            power: 幂次
            
        Returns:
            矩阵的幂运算结果
        """
        try:
            if not matrix or len(matrix) != len(matrix[0]):
                raise ValueError("输入必须是方阵")
                
            if power == 0:
                # 单位矩阵
                n = len(matrix)
                return [[1 if i == j else 0 for j in range(n)] for i in range(n)]
            elif power == 1:
                # 矩阵本身
                return [row[:] for row in matrix]
            elif power > 1:
                # 矩阵连乘
                result = [row[:] for row in matrix]
                for _ in range(power - 1):
                    result = self.matrix_multiply(result, matrix)
                return result
            else:
                raise ValueError("幂次必须是非负整数")
                
        except Exception as e:
            print(f"Error in matrix_power: {e}")
            return []
    
    def hadamard_product(self, matrix1: List[List[Union[int, float]]], 
                        matrix2: List[List[Union[int, float]]]) -> List[List[Union[int, float]]]:
        """
        Hadamard积（逐元素乘积）
        
        Args:
            matrix1: 第一个矩阵
            matrix2: 第二个矩阵
            
        Returns:
            Hadamard积结果矩阵
        """
        try:
            if not matrix1 or not matrix2:
                print("Warning: 矩阵不能为空")
                return []
                
            # 检查矩阵尺寸是否匹配
            if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
                raise ValueError("矩阵尺寸不匹配")
                
            result = []
            for i in range(len(matrix1)):
                row = []
                for j in range(len(matrix1[0])):
                    try:
                        val1 = float(matrix1[i][j]) if matrix1[i][j] is not None else 0
                        val2 = float(matrix2[i][j]) if matrix2[i][j] is not None else 0
                        row.append(val1 * val2)
                    except (ValueError, TypeError):
                        print(f"Warning: 位置({i},{j})的元素无法转换为数字，使用0代替")
                        row.append(0)
                result.append(row)
                
            return result
            
        except Exception as e:
            print(f"Error in hadamard_product: {e}")
            return []
    
    def matrix_concatenate(self, matrix1: List[List[Any]], 
                          matrix2: List[List[Any]], 
                          axis: int = 0) -> List[List[Any]]:
        """
        矩阵拼接
        
        Args:
            matrix1: 第一个矩阵
            matrix2: 第二个矩阵
            axis: 拼接轴 (0: 垂直拼接, 1: 水平拼接)
            
        Returns:
            拼接后的矩阵
        """
        try:
            if not matrix1 or not matrix2:
                print("Warning: 矩阵不能为空")
                return []
                
            if axis == 0:
                # 垂直拼接（行数增加）
                if len(matrix1[0]) != len(matrix2[0]):
                    raise ValueError("矩阵列数不匹配，无法垂直拼接")
                return matrix1 + matrix2
                
            elif axis == 1:
                # 水平拼接（列数增加）
                if len(matrix1) != len(matrix2):
                    raise ValueError("矩阵行数不匹配，无法水平拼接")
                result = []
                for i in range(len(matrix1)):
                    result.append(matrix1[i] + matrix2[i])
                return result
                
            else:
                raise ValueError("轴参数必须是0或1")
                
        except Exception as e:
            print(f"Error in matrix_concatenate: {e}")
            return []
    
    def extract_submatrix(self, matrix: List[List[Any]], 
                        start_row: int, start_col: int, 
                        end_row: int, end_col: int) -> List[List[Any]]:
        """
        提取子矩阵
        
        Args:
            matrix: 输入矩阵
            start_row: 起始行索引
            start_col: 起始列索引
            end_row: 结束行索引（包含）
            end_col: 结束列索引（包含）
            
        Returns:
            提取的子矩阵
        """
        try:
            if not matrix:
                print("Warning: 矩阵不能为空")
                return []
                
            # 验证索引范围
            if (start_row < 0 or start_col < 0 or 
                end_row >= len(matrix) or end_col >= len(matrix[0]) or
                start_row > end_row or start_col > end_col):
                raise ValueError("索引范围无效")
                
            result = []
            for i in range(start_row, end_row + 1):
                row = []
                for j in range(start_col, end_col + 1):
                    row.append(matrix[i][j])
                result.append(row)
                
            return result
            
        except Exception as e:
            print(f"Error in extract_submatrix: {e}")
            return []


def get_list_2d_math():
    """获取List2DMath实例"""
    return List2DMath()
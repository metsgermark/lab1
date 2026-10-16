"""Заготовки задач на NumPy."""

import numpy as np
from grader_contracts.numpy_tasks import (
    BinarizeInput, ChessInput, EllipseInput, MatrixInput, MatrixStatistics,
    MatrixVectorBatchInput, OneHotInput, RandomMatrixInput, RectangleInput,
    TimeSeriesInput, TimeSeriesStatistics,
)


def sum_prod(data: MatrixVectorBatchInput) -> np.ndarray:
    matrices, vectors = data.matrices, data.vectors
    result = np.zeros_like(vectors[0])
    for matrix, vector in zip(matrices, vectors):
        result += matrix @ vector
    return result


def binarize(data: BinarizeInput) -> np.ndarray:
    matrix, threshold = data.matrix, data.threshold
    return (matrix > threshold).astype(float)


def unique_rows(data: MatrixInput) -> list[list[float]]:
    matrix = data.matrix
    result = []
    for row in matrix:
        result.append(list(np.unique(row)))
    return result


def unique_columns(data: MatrixInput) -> list[list[float]]:
    matrix = data.matrix
    result = []
    for col in matrix.T:
        result.append(list(np.unique(col)))
    return result


def matrix_statistics(data: RandomMatrixInput) -> MatrixStatistics:
    rows, columns, mean, std, seed = data.rows, data.columns, data.mean, data.std, data.seed
    np.random.seed(seed)
    matrix = np.random.normal(mean, std, (rows, columns))
    
    row_means = np.mean(matrix, axis=1)
    column_means = np.mean(matrix, axis=0)
    row_variances = np.var(matrix, axis=1)
    column_variances = np.var(matrix, axis=0)
    
    return MatrixStatistics(
        matrix=matrix,
        row_means=row_means,
        column_means=column_means,
        row_variances=row_variances,
        column_variances=column_variances
    )



def chess(data: ChessInput) -> np.ndarray:
    rows, columns, first, second = data.rows, data.columns, data.first, data.second
    matrix = np.zeros((rows, columns))
    for i in range(rows):
        for j in range(columns):
            if (i + j) % 2 == 0:
                matrix[i, j] = first
            else:
                matrix[i, j] = second
    return matrix

def draw_rectangle(data: RectangleInput) -> np.ndarray:
    width, height = data.width, data.height
    image_height, image_width = data.image_height, data.image_width
    shape_color, background_color = data.shape_color, data.background_color

    image = np.full((image_height, image_width, 3), background_color, dtype=float)
    
    start_y = (image_height - height) // 2
    start_x = (image_width - width) // 2
    end_y = start_y + height
    end_x = start_x + width
    
    image[start_y:end_y, start_x:end_x] = shape_color
    
    return image


def draw_ellipse(data: EllipseInput) -> np.ndarray:
    semi_axis_x, semi_axis_y = data.semi_axis_x, data.semi_axis_y
    image_height, image_width = data.image_height, data.image_width
    shape_color, background_color = data.shape_color, data.background_color

    image = np.full((image_height, image_width, 3), background_color, dtype=float)
    x0, y0 = image_width // 2, image_height // 2  
    y, x = np.ogrid[:image_height, :image_width] 
    mask = ((x - x0) / semi_axis_x) ** 2 + ((y - y0) / semi_axis_y) ** 2 <= 1
    image[mask] = shape_color
    
    return image


def analyze_time_series(data: TimeSeriesInput) -> TimeSeriesStatistics:
    values, window = data.values, data.window
    mean = np.mean(values)
    variance = np.var(values)
    std = np.std(values)
    
    local_maxima = []
    for i in range(1, len(values) - 1):
        if values[i] > values[i-1] and values[i] > values[i+1]:
            local_maxima.append(i)
    
    local_minima = []
    for i in range(1, len(values) - 1):
        if values[i] < values[i-1] and values[i] < values[i+1]:
            local_minima.append(i)
    
    moving_avg = []
    for i in range(len(values) - window + 1):
        moving_avg.append(np.mean(values[i:i+window]))
    
    return TimeSeriesStatistics(
        mean=mean,
        variance=variance,
        std=std,
        local_maxima_indices=local_maxima,
        local_minima_indices=local_minima,
        moving_average=moving_avg
    )


def one_hot(data: OneHotInput) -> np.ndarray:
    labels, class_count = data.labels, data.class_count
    if class_count is None:
        class_count = int(np.max(labels)) + 1
    
    n_samples = len(labels)
    one_hot_matrix = np.zeros((n_samples, class_count))
    
    for i, label in enumerate(labels):
        one_hot_matrix[i, label] = 1
    
    return one_hot_matrix

# проверка функции sum_prod

'''
matrices = [np.array([[1, 2], [3, 4]]), np.array([[0, 1], [1, 0]])]
vectors = [np.array([1, 0]), np.array([2, 3])]
result = sum_prod(MatrixVectorBatchInput(matrices, vectors))
print (result) # [4 5]

'''
# проверка функции binarize

'''
matrix = np.array([[1.0, 5.0], [3.0, 3.0]])
result = binarize(BinarizeInput(matrix, 3.0))
print(result) #[[0. 1.]
                # [0. 0.]]

'''

# проверка функции unique_rows и unique_columns

'''
matrix = np.array([[2, 1, 2, 3], [4, 4, 4, 1]])
result = unique_rows(MatrixInput(matrix))
print(result) # [[np.int64(1), np.int64(2), np.int64(3)], [np.int64(1), np.int64(4)]] ([[1,2,3][1,4]])

matrix = np.array([[1, 2], [1, 3], [2, 3]])
result = unique_columns(MatrixInput(matrix))
print(result) #[[np.int64(1), np.int64(2)], [np.int64(2), np.int64(3)]] ([[1,2][2,3]])

'''

# проверка функции matrix_statistics

'''
result = matrix_statistics(RandomMatrixInput(rows=3, columns=2, mean=0.0, std=1.0, seed=42))
print(f"row_means: {result.row_means}") # row_means: [ 0.17922493  1.0853592  -0.23414517]
print(f"column_means: {result.column_means}") # column_means: [0.30341644 0.38354287]
print(f"row_variances: {result.row_variances}") # row_variances: [1.00799409e-01 1.91555606e-01 6.73858271e-11]
print(f"column_variances: {result.column_variances}") # column_variances: [0.14828953 0.65074723]

'''
# проверка функции chess

'''
result = chess(ChessInput(rows=3, columns=4, first=0, second=1))
print(f"chess:\n{result}")
#[[0. 1. 0. 1.]
#[1. 0. 1. 0.]
#[0. 1. 0. 1.]]

'''
# проверка функций draw_rectangle и draw_ellipse

'''
result = draw_rectangle(RectangleInput(
    width=2, height=2, image_height=4, image_width=4,
    shape_color=[255, 0, 0], background_color=[0, 0, 0]
))
print(f"draw_rectangle: форма = {result.shape} ") # draw_rectangle: форма = (4, 4, 3) 
print(f"Цвет в центре (1,1): {result[1, 1]}  ") # Цвет в центре (1,1): [255.   0.   0.]  
print(f"Цвет на углу (0,0): {result[0, 0]}  ") # Цвет на углу (0,0): [0. 0. 0.] 

result = draw_ellipse(EllipseInput(
    semi_axis_x=2, semi_axis_y=2, image_height=5, image_width=5,
    shape_color=[0, 255, 0], background_color=[0, 0, 0]
))
print(f"draw_ellipse: форма = {result.shape}  ") # draw_ellipse: форма = (5, 5, 3)
print(f"Цвет в центре (2,2): {result[2, 2]}  ") # Цвет в центре (2,2): [  0. 255.   0.]
print(f"Цвет на углу (0,0): {result[0, 0]}  ") # Цвет на углу (0,0): [0. 0. 0.]

'''

# проверка функции analyze_time_series

'''

result = analyze_time_series(TimeSeriesInput(
    values=np.array([10.0, 30.0, 20.0, 40.0, 10.0]), window=2
))
print(f"mean: {result.mean} ") # mean: 22.0 
print(f"variance: {result.variance} ") # variance: 136.0
print(f"std: {result.std} ") # std: 11.661903789690601
print(f"local_maxima: {result.local_maxima_indices} ") # local_maxima: [1, 3]
print(f"local_minima: {result.local_minima_indices} ") # local_minima: [2]
print(f"moving_avg: {result.moving_average} ") 
# moving_avg: [np.float64(20.0), np.float64(25.0), np.float64(30.0), np.float64(25.0)]

'''
# проверка функции one_hot

'''
result = one_hot(OneHotInput(labels=[0, 2, 3, 0], class_count=None))
print(f"one_hot:\n{result}") #one_hot:
                               # [[1. 0. 0. 0.]
                               # [0. 0. 1. 0.]
                               # [0. 0. 0. 1.]
                               # [1. 0. 0. 0.]]

'''
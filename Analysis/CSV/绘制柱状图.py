import matplotlib.pyplot as plt
import numpy as np
import os
import random


# 生成互不相似的随机颜色
def generate_distinct_colors(num_colors):
    colors = []
    for i in range(num_colors):
        color = "#"+''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
        while color in colors:
            color = "#"+''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
        colors.append(color)
    return colors

# def generate_distinct_colors(num_colors):
#     base_colors = ["#FFA500", "#008000", "#FF0000", "#00FFFF"]
#     colors = []
#     for i in range(num_colors):
#         colors.append(base_colors[i % len(base_colors)])
#     return colors

def compare_performance_test(models, accuracy, precision, recall, f1_score):
    # 指标列表和颜色
    metrics = [accuracy, precision, recall, f1_score]
    metric_names = ['Accuracy', 'Precision', 'Recall', 'F1 Score']
    colors = generate_distinct_colors(len(metric_names))
    # 绘制柱状图
    plt.figure(figsize=(10, 6))

    bar_width = 0.2
    index = np.arange(len(models))

    for i, (metric, color, metric_name) in enumerate(zip(metrics[::-1], colors[::-1], metric_names[::-1])):
        plt.barh(index + i * bar_width, metric, bar_width, label=metric_name, color=color)

    # 在每个柱状图上方添加数值标签
    # for i, metric in enumerate(metrics[::-1]):
    #     for j, value in enumerate(metric):
    #         plt.text(value + 0.01, j + i * bar_width, round(value, 2), va='center')

    # 设置Y轴标签和刻度
    plt.yticks(index + bar_width, models)
    plt.xlabel('Metrics')
    plt.title('Model Performance Comparison')

    # 保持图注顺序不变
    handles, labels = plt.gca().get_legend_handles_labels()
    plt.legend(handles[::-1], labels[::-1], loc='center left', bbox_to_anchor=(1, 0.5))  # 图注放到图像外面

    # 设置X轴坐标范围为0到1
    plt.xlim(0.75, 1)

    # # 显示图形
    # plt.show()
    # 保存路径
    plt.savefig(os.path.join(r'./', "Test_performance_compare.png"), dpi=300, bbox_inches='tight')


def get_data(my_data):
    models = []  # 可以修改为实际的模型名称
    accuracy = []  # 准确率
    precision = []  # 精确率
    recall = []  # 召回率
    f1_score = []  # F1值
    for one_data in my_data:
        models.append(one_data['name'])
        accuracy.append(one_data['accuracy'])
        precision.append(one_data['precision'])
        recall.append(one_data['recall'])
        f1_score.append(one_data['f1_score'])
    return models, accuracy, precision, recall, f1_score


if __name__ == '__main__':
    my_data = [
    {
        'name': 'Improve_ConvNeXt',
        'accuracy': 0.9727,
        'precision': 0.9614,
        'recall': 0.9578,
        'f1_score': 0.9596,
    },
    {
        'name': 'Model_AlexNet',
        'accuracy': 0.8965,
        'precision': 0.8682,
        'recall': 0.8654,
        'f1_score': 0.8652,
    },
    {
        'name': 'Model_ConvNeXt',
        'accuracy': 0.9705,
        'precision': 0.9611,
        'recall': 0.956,
        'f1_score': 0.9585,
    },
    {
        'name': 'Model_DenseNet',
        'accuracy': 0.9648,
        'precision': 0.9487,
        'recall': 0.9497,
        'f1_score': 0.9491,
    },
    {
        'name': 'Model_EfficientNet',
        'accuracy': 0.9531,
        'precision': 0.9348,
        'recall': 0.9328,
        'f1_score': 0.9336,
    },
    {
        'name': 'Model_GoogLeNet',
        'accuracy': 0.9453,
        'precision': 0.9198,
        'recall': 0.9216,
        'f1_score': 0.9201,
    },
    {
        'name': 'Model_MobileNet',
        'accuracy': 0.9375,
        'precision': 0.9141,
        'recall': 0.9183,
        'f1_score': 0.9159,
    },
    {
        'name': 'Model_RegNet',
        'accuracy': 0.957,
        'precision': 0.9339,
        'recall': 0.9375,
        'f1_score': 0.9356,
    },
    {
        'name': 'Model_ResNet',
        'accuracy': 0.957,
        'precision': 0.937,
        'recall': 0.9362,
        'f1_score': 0.9362,
    },
    {
        'name': 'Model_ShuffleNet',
        'accuracy': 0.9512,
        'precision': 0.9295,
        'recall': 0.9343,
        'f1_score': 0.9297,
    },
    {
        'name': 'Model_Swin_Transformer',
        'accuracy': 0.959,
        'precision': 0.9384,
        'recall': 0.9373,
        'f1_score': 0.9374,
    },
    {
        'name': 'Model_VGG',
        'accuracy': 0.834,
        'precision': 0.8102,
        'recall': 0.7987,
        'f1_score': 0.8021,
    },
]
    # 模型名称和对应的各项指标
    models, accuracy, precision, recall, f1_score = get_data(my_data)
    compare_performance_test(models, accuracy, precision, recall, f1_score)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          import matplotlib.pyplot as plt
import numpy as np
import os
import random


# 生成互不相似的随机颜色
def generate_distinct_colors(num_colors):
    colors = []
    for i in range(num_colors):
        color = "#"+''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
        while color in colors:
            color = "#"+''.join([random.choice('0123456789ABCDEF') for _ in range(6)])
        colors.append(color)
    return colors

# def generate_distinct_colors(num_colors):
#     base_colors = ["#FFA500", "#008000", "#FF0000", "#00FFFF"]
#     colors = []
#     for i in range(num_colors):
#         colors.append(base_colors[i % len(base_colors)])
#     return colors

def compare_performance_test(models, accuracy, precision, recall, f1_score):
    # 指标列表和颜色
    metrics = [accuracy, precision, recall, f1_score]
    metric_names = ['Accuracy', 'Precision', 'Recall', 'F1 Score']
    colors = generate_distinct_colors(len(metric_names))
    # 绘制柱状图
    plt.figure(figsize=(10, 6))

    bar_width = 0.2
    index = np.arange(len(models))

    for i, (metric, color, metric_name) in enumerate(zip(metrics[::-1], colors[::-1], metric_names[::-1])):
        plt.barh(index + i * bar_width, metric, bar_width, label=metric_name, color=color)

    # 在每个柱状图上方添加数值标签
    # for i, metric in enumerate(metrics[::-1]):
    #     for j, value in enumerate(metric):
    #         plt.text(value + 0.01, j + i * bar_width, round(value, 2), va='center')

    # 设置Y轴标签和刻度
    plt.yticks(index + bar_width, models)
    plt.xlabel('Metrics')
    plt.title('Model Performance Comparison')

    # 保持图注顺序不变
    handles, labels = plt.gca().get_legend_handles_labels()
    plt.legend(handles[::-1], labels[::-1], loc='center left', bbox_to_anchor=(1, 0.5))  # 图注放到图像外面

    # 设置X轴坐标范围为0到1
    plt.xlim(0.75, 1)

    # # 显示图形
    # plt.show()
    # 保存路径
    plt.savefig(os.path.join(r'./', "Test_performance_compare.png"), dpi=300, bbox_inches='tight')


def get_data(my_data):
    models = []  # 可以修改为实际的模型名称
    accuracy = []  # 准确率
    precision = []  # 精确率
    recall = []  # 召回率
    f1_score = []  # F1值
    for one_data in my_data:
        models.append(one_data['name'])
        accuracy.append(one_data['accuracy'])
        precision.append(one_data['precision'])
        recall.append(one_data['recall'])
        f1_score.append(one_data['f1_score'])
    return models, accuracy, precision, recall, f1_score


if __name__ == '__main__':
    my_data = [
    {
        'name': 'Improve_ConvNeXt',
        'accuracy': 0.9727,
        'precision': 0.9614,
        'recall': 0.9578,
        'f1_score': 0.9596,
    },
    {
        'name': 'Model_AlexNet',
        'accuracy': 0.8965,
        'precision': 0.8682,
        'recall': 0.8654,
        'f1_score': 0.8652,
    },
    {
        'name': 'Model_ConvNeXt',
        'accuracy': 0.9705,
        'precision': 0.9611,
        'recall': 0.956,
        'f1_score': 0.9585,
    },
    {
        'name': 'Model_DenseNet',
        'accuracy': 0.9648,
        'precision': 0.9487,
        'recall': 0.9497,
        'f1_score': 0.9491,
    },
    {
        'name': 'Model_EfficientNet',
        'accuracy': 0.9531,
        'precision': 0.9348,
        'recall': 0.9328,
        'f1_score': 0.9336,
    },
    {
        'name': 'Model_GoogLeNet',
        'accuracy': 0.9453,
        'precision': 0.9198,
        'recall': 0.9216,
        'f1_score': 0.9201,
    },
    {
        'name': 'Model_MobileNet',
        'accuracy': 0.9375,
        'precision': 0.9141,
        'recall': 0.9183,
        'f1_score': 0.9159,
    },
    {
        'name': 'Model_RegNet',
        'accuracy': 0.957,
        'precision': 0.9339,
        'recall': 0.9375,
        'f1_score': 0.9356,
    },
    {
        'name': 'Model_ResNet',
        'accuracy': 0.957,
        'precision': 0.937,
        'recall': 0.9362,
        'f1_score': 0.9362,
    },
    {
        'name': 'Model_ShuffleNet',
        'accuracy': 0.9512,
        'precision': 0.9295,
        'recall': 0.9343,
        'f1_score': 0.9297,
    },
    {
        'name': 'Model_Swin_Transformer',
        'accuracy': 0.959,
        'precision': 0.9384,
        'recall': 0.9373,
        'f1_score': 0.9374,
    },
    {
        'name': 'Model_VGG',
        'accuracy': 0.834,
        'precision': 0.8102,
        'recall': 0.7987,
        'f1_score': 0.8021,
    },
]
    # 模型名称和对应的各项指标
    models, accuracy, precision, recall, f1_score = get_data(my_data)
    compare_performance_test(models, accuracy, precision, recall, f1_score)

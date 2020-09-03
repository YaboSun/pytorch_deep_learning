import pandas as pd
"""
感知器实现简单逻辑运算：AND,OR,NOT,XOR
"""
W1 = 1.0
W2 = 1.0
Bias = -2.0

# generate and check output
def AND(test_inputs, test_outputs):
    """
    首先，线性组合就是权重与输入的点积：linear_combination = weight1*input1 + weight2*input2，然后我们把值带入单位阶跃函数与偏置项相结合，给到我们一个（0 或 1）的输出
    """
    outputs = []
    for idx in range(len(test_inputs)): 
        test_input = test_inputs[idx]   
        correct_output = test_outputs[idx]
        linear_combination = W1 * test_input[0] + W2 * test_input[1] + Bias
        output = int(linear_combination >= 0)
        if output == correct_output:
            is_correct_string = 'Yes'
        else:
            is_correct_string = 'no'
        outputs.append([test_input[0], test_input[1], linear_combination, output, is_correct_string])
    
    return outputs

def print_output(outputs):
    # Print output
    num_wrong = len([output[4] for output in outputs if output[4] == 'No'])
    output_frame = pd.DataFrame(outputs, columns=['Input 1', '  Input 2', '  Linear Combination', '  Activation Output', '  Is Correct'])
    if not num_wrong:
        print('Nice!  You got it all correct.\n')
    else:
        print('You got {} wrong.  Keep trying!\n'.format(num_wrong))
    print(output_frame.to_string(index=False))

if __name__ == "__main__":
    test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    test_outputs = [False, False, False, True]
    outputs = AND(test_inputs, test_outputs)
    print_output(outputs)

    
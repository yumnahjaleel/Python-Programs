import random

#LogicPerceptron.py
#This program doesn't just run; it learns how to be an OR Gate by looking at examples.

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1):
        # Initialize weights and bias with small random numbers
        self.weights = [random.uniform(-1, 1) for _ in range(input_size)]
        self.bias = random.uniform(-1, 1)
        self.lr = learning_rate

    def predict(self, inputs):
        # Step 1: Weighted Sum (Dot Product)
        total_sum = sum(i * w for i, w in zip(inputs, self.weights)) + self.bias
        
        # Step 2: Activation Function (Heaviside Step Function)
        return 1 if total_sum > 0 else 0

    def train(self, training_data, labels, epochs=100):
        for epoch in range(epochs):
            total_error = 0
            for inputs, label in zip(training_data, labels):
                prediction = self.predict(inputs)
                error = label - prediction
                total_error += abs(error)

                # Step 3: Weight Update Logic (Learning)
                # weight = weight + (learning_rate * error * input)
                for i in range(len(self.weights)):
                    self.weights[i] += self.lr * error * inputs[i]
                self.bias += self.lr * error
            
            if total_error == 0:
                print(f"Converged at epoch {epoch}")
                break

# --- Training the AI to be an 'OR' Gate ---
# Inputs: [0,0], [0,1], [1,0], [1,1]
# Labels:   0,     1,     1,     1
training_inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
labels = [0, 1, 1, 1]

model = Perceptron(input_size=2)

print("Pre-training prediction for [1, 1]:", model.predict([1, 1]))

model.train(training_inputs, labels)

print("\n--- Post-Training Truth Table Check ---")
for inputs in training_inputs:
    print(f"Input: {inputs} | AI Prediction: {model.predict(inputs)}")

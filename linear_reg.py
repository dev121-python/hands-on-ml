import math

# -----------------------------
# Dataset (learnable)
# -----------------------------
X = [
    [0, 0, 0, 1],
    [0, 1, 1, 1],
    [1, 1, 1, 1]
]
y = [0, 0, 1]
def sigmoid(z):
    return 1/(1+math.exp(-z))
def predict_proba(X ,W,b):
    p = 0

    z = 0
    for i in range(len(X)):

        z += X[i]*W[i]
    z+= b
    return sigmoid(z)

w = [0.0, 0.0, 0.0, 0.0]
b = 0.0
learning_rate = 0.1
epochs = 1000
eps = 1e-15
for epoch in range(epochs):
    total_loss = 0
    for i in range (len(X)):
        pred_y = predict_proba(X[i],w,b)
        pred_y = max(eps,min(1-eps,pred_y))
        loss = -(y[i]*math.log(pred_y) + (1-y[i])*math.log(1-pred_y))
        total_loss += loss

        diff = pred_y - y[i]
        for j in range(len(w)):
            w[j] -= learning_rate*X[i][j]*diff
        b -= learning_rate*diff
    if epoch % 100 == 0:
        print(f"epoch={epoch}, loss={total_loss/len(X):.4f}")
def predict(x,w,b,threshold=0.5):
    if predict_proba(x,w,b) > threshold:
        return 1
    else:
        return 0
correct = 0
    
for i in range(len(X)):
    if predict(X[i], w, b) == y[i]:
        correct += 1
accuracy = correct/len(X)

print("\nTraining accuracy:", accuracy)

# -----------------------------
# Test prediction
# -----------------------------
X_test = [1, 2, 3, 4]
prob = predict_proba(X_test, w, b)
pred = predict(X_test, w, b)

print("\nTest sample:", X_test)
print("Predicted probability:", prob)
print("Predicted class:", pred)
from sklearn.svm import SVC


def cost_function(x, X_train, y_train, X_test, y_test, threshold):
    """
    default cost function based on sklearn.svm.SVC
    """
    columns = X_train.columns.to_numpy()
    selected_cols = columns[x > threshold]
    selected_count = selected_cols.size
    if selected_count == 0:
        return 1

    svm = SVC()
    svm.fit(X_train[selected_cols],
            y_train.values.ravel())
    acc = svm.score(X_test[selected_cols], y_test)
    g = selected_count / x.size
    f = 1 - (acc - g)
    return f

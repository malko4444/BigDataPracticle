import numpy as np  

a = np.array([[3, 4, 5, 6, 7], [1, 2, 3, 4, 5]])  
print("Dimensions:" + str(a.ndim))

print("Shape:" + str(a.shape))
print(a[0,1])

# -------------------------------------

b = np.array([[23, 42, 45, 11, 10],[23, 43, 1, 9, 10]])
print("Dimensions:" + str(b.ndim))
print(b[0, 4])
# acces 9 in 2d array
print(b[1, 3])

# -------------------------------------

import numpy as np

c = np.array([
    [
        [  # First 3D block
            [3, 8, 2, 4],
            [2, 7, 9, 3],
            [1, 2, 3, 4],
            [9, 1, 2, 4]
        ],
        [  # Second 3D block
            [3, 8, 2, 4],
            [2, 7, 9, 3],
            [1, 2, 3, 4],
            [9, 1, 2, 4]
        ]
    ],
    [
        [  # Third 3D block
            [3, 8, 2, 4],
            [2, 7, 9, 3],
            [1, 2, 3, 4],
            [9, 1, 2, 4]
        ],
        [  # Fourth 3D block
            [3, 8, 2, 4],
            [2, 7, 9, 3],
            [1, 2, 3, 4],
            [9, 1, 2, 4]
        ]
    ]
])
print("Dimension:"+ str(c.ndim))
print("Shape:" + str(c.shape))
print(c[1,1,2,1])
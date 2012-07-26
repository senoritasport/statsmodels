import numpy as np

class Bunch(dict):
    def __init__(self, **kw):
        dict.__init__(self, kw)
        self.__dict__  = self


RSUR = Bunch()
RSUR.call = '''systemfit(formula = formula, method = "SUR", data = panel, methodResidCov = "noDfCor")'''
RSUR.params = np.squeeze(np.array([
     0.9979992, 0.06886083, 0.3083878, -21.1374, 0.03705313, 0.1286866,
     -168.1134, 0.1219063, 0.3821666, 62.25631, 0.1214024, 0.3691114,
     1.407487, 0.05635611, 0.04290209
    ]).reshape(15,1, order='F'))
RSUR.cov_params = np.array([
     133.7852, -0.1840371, 0.01059675, -31.21063, 0.01337293, 0.01044742,
     -161.6206, 0.0343593, -0.002197769, 158.6378, -0.06916984,
     -0.01307428, 0.03036482, 6.95277e-05, 0.006869873, -0.1840371,
     0.0002886686, -0.0001325481, 0.03921905, -1.927362e-05, -4.504895e-06,
     0.199845, -5.161935e-05, 3.680446e-05, -0.1667078, 0.0001043746,
     -0.0001326094, 0.002294617, -1.738464e-06, -1.317451e-05, 0.01059675,
     -0.0001325481, 0.0006704354, 0.02437061, -1.011555e-07, -6.041142e-05,
     0.07380307, 1.174274e-05, -0.0001923003, -0.2035738, -2.6258e-05,
     0.0008660189, -0.00788213, 9.366098e-06, 1.866325e-05, -31.21063,
     0.03921905, 0.02437061, 635.1519, -0.2770547, -0.160579, 582.7983,
     -0.1213974, -0.04056555, 716.5924, -0.2598967, -0.5263574, 100.0872,
     -0.1653628, 0.2297848, 0.01337293, -1.927362e-05, -1.011555e-07,
     -0.2770547, 0.0001458083, -1.501036e-05, -0.2645839, 6.420246e-05,
     -2.106559e-05, -0.3380538, 0.0001551097, 0.000109222, -0.038997,
     8.497461e-05, -0.0002103376, 0.01044742, -4.504895e-06, -6.041142e-05,
     -0.160579, -1.501036e-05, 0.0004741078, -0.09690712, -8.097892e-06,
     0.0002035703, -0.02848283, -0.0001030127, 0.0007854907, -0.03888171,
     9.981992e-07, 0.0004461934, -161.6206, 0.199845, 0.07380307, 582.7983,
     -0.2645839, -0.09690712, 8026.788, -1.849853, 0.5369888, -1593.177,
     0.7497236, 0.05596429, 108.7601, -0.2004693, 0.3741887, 0.0343593,
     -5.161935e-05, 1.174274e-05, -0.1213974, 6.420246e-05, -8.097892e-06,
     -1.849853, 0.0004695548, -0.0002854946, 0.3432181, -0.0001922897,
     0.0001219025, -0.0226266, 4.929475e-05, -0.0001219727, -0.002197769,
     3.680446e-05, -0.0001923003, -0.04056555, -2.106559e-05, 0.0002035703,
     0.5369888, -0.0002854946, 0.001079986, 0.01136712, 0.0001289726,
     -0.0009010479, -0.006771958, -2.030504e-05, 0.0002381459, 158.6378,
     -0.1667078, -0.2035738, 716.5924, -0.3380538, -0.02848283, -1593.177,
     0.3432181, 0.01136712, 11369.52, -5.187909, -2.525447, 256.2028,
     -0.4783715, 1.054605, -0.06916984, 0.0001043746, -2.6258e-05,
     -0.2598967, 0.0001551097, -0.0001030127, 0.7497236, -0.0001922897,
     0.0001289726, -5.187909, 0.002739435, -0.0007250238, -0.08272505,
     0.0002158356, -0.0007249087, -0.01307428, -0.0001326094, 0.0008660189,
     -0.5263574, 0.000109222, 0.0007854907, 0.05596429, 0.0001219025,
     -0.0009010479, -2.525447, -0.0007250238, 0.0134136, -0.2289551,
     0.0001790085, 0.001271094, 0.03036482, 0.002294617, -0.00788213,
     100.0872, -0.038997, -0.03888171, 108.7601, -0.0226266, -0.006771958,
     256.2028, -0.08272505, -0.2289551, 39.2104, -0.06063476, 0.0689298,
     6.95277e-05, -1.738464e-06, 9.366098e-06, -0.1653628, 8.497461e-05,
     9.981992e-07, -0.2004693, 4.929475e-05, -2.030504e-05, -0.4783715,
     0.0002158356, 0.0001790085, -0.06063476, 0.0001316823, -0.0003235898,
     0.006869873, -1.317451e-05, 1.866325e-05, 0.2297848, -0.0002103376,
     0.0004461934, 0.3741887, -0.0001219727, 0.0002381459, 1.054605,
     -0.0007249087, 0.001271094, 0.0689298, -0.0003235898, 0.001730147
    ]).reshape(15,15, order='F')
RSUR.cov_params_rownames = ['Chrysler_(Intercept)', 'Chrysler_value', 'Chrysler_capital', 'General.Electric_(Intercept)', 'General.Electric_value', 'General.Electric_capital', 'General.Motors_(Intercept)', 'General.Motors_value', 'General.Motors_capital', 'US.Steel_(Intercept)', 'US.Steel_value', 'US.Steel_capital', 'Westinghouse_(Intercept)', 'Westinghouse_value', 'Westinghouse_capital', ]
RSUR.cov_params_colnames = ['Chrysler_(Intercept)', 'Chrysler_value', 'Chrysler_capital', 'General.Electric_(Intercept)', 'General.Electric_value', 'General.Electric_capital', 'General.Motors_(Intercept)', 'General.Motors_value', 'General.Motors_capital', 'US.Steel_(Intercept)', 'US.Steel_value', 'US.Steel_capital', 'Westinghouse_(Intercept)', 'Westinghouse_value', 'Westinghouse_capital', ]
RSUR.cov_resids_est = np.array([
     149.8722, -21.37565, -282.7564, 367.8402, 13.30695, -21.37565,
     660.8294, 607.5331, 978.4503, 176.4491, -282.7564, 607.5331, 7160.294,
     -1967.046, 126.1762, 367.8402, 978.4503, -1967.046, 7904.663,
     511.4995, 13.30695, 176.4491, 126.1762, 511.4995, 88.6617
    ]).reshape(5,5, order='F')
RSUR.cov_resids_est_rownames = ['Chrysler', 'General.Electric', 'General.Motors', 'US.Steel', 'Westinghouse', ]
RSUR.cov_resids_est_colnames = ['Chrysler', 'General.Electric', 'General.Motors', 'US.Steel', 'Westinghouse', ]
RSUR.cov_resids = np.array([
     153.2369, 3.147771, -315.6107, 414.5298, 16.64749, 3.147771, 704.729,
     601.6316, 1298.695, 201.4385, -315.6107, 601.6316, 7222.22, -2446.317,
     129.7644, 414.5298, 1298.695, -2446.317, 8174.28, 613.9925, 16.64749,
     201.4385, 129.7644, 613.9925, 94.90675
    ]).reshape(5,5, order='F')
RSUR.cov_resids_rownames = ['Chrysler', 'General.Electric', 'General.Motors', 'US.Steel', 'Westinghouse', ]
RSUR.cov_resids_colnames = ['Chrysler', 'General.Electric', 'General.Motors', 'US.Steel', 'Westinghouse', ]
RSUR.method = 'SUR'
RSUR.rank = 15
RSUR.df_resid = 85
RSUR.iter = 1
RSUR.panelLike = '''TRUE'''
RSUR.fittedvalues = np.array([
     32.98547, 61.83516, 72.56515, 47.12665, 67.63205, 71.80774, 68.5076,
     51.31181, 62.20854, 67.74787, 76.11978, 88.6971, 70.72036, 82.81307,
     87.10292, 99.08188, 119.4633, 140.6773, 176.6952, 177.371, 34.82255,
     66.98919, 97.91866, 74.54072, 84.67318, 81.88021, 75.24862, 74.73898,
     84.85019, 82.72565, 94.38241, 105.2126, 98.98109, 108.2389, 111.4822,
     121.8484, 132.6644, 149.3613, 169.7257, 195.5151, 208.2453, 420.2794,
     548.5702, 252.2227, 435.4257, 477.1924, 484.2357, 343.427, 426.9885,
     442.7958, 523.2972, 583.0448, 552.8092, 581.1657, 672.8126, 709.7192,
     882.6026, 978.9525, 1272.014, 1364.599, 247.5132, 300.2828, 430.7577,
     377.0541, 415.2984, 423.5218, 447.7405, 435.7832, 414.6501, 385.4872,
     365.7911, 362.2243, 378.1208, 372.9127, 394.2292, 397.9648, 466.4802,
     488.372, 539.0389, 566.277, 12.27691, 30.52156, 42.80857, 33.76598,
     31.71523, 37.96421, 33.22941, 35.64298, 39.81141, 40.63853, 46.91736,
     47.95589, 38.93935, 44.33515, 40.3917, 43.0696, 47.76244, 56.34706,
     76.16779, 77.56886
    ])



RSURI = Bunch()
RSURI.call = '''systemfit(formula = formula, method = "SUR", data = panel, methodResidCov = "noDfCor",      maxiter = 100, tol = 1e-04)'''
RSURI.params = np.squeeze(np.array([
     3.297673, 0.06622757, 0.3044762, -14.84538, 0.03669229, 0.1147134,
     -184.4875, 0.1246316, 0.3892042, 113.5387, 0.1072072, 0.2901168,
     4.711002, 0.05316157, 0.02935392
    ]).reshape(15,1, order='F'))
RSURI.cov_params = np.array([
     135.806, -0.1870255, 0.01359519, -24.56835, 0.01068199, 0.01128718,
     -151.2304, 0.03113382, -0.0008632869, 123.4479, -0.05306735,
     0.01009713, -2.477967, 0.004861604, 0.002005951, -0.1870255,
     0.0002940712, -0.0001387899, 0.03599721, -1.627649e-05, -1.099374e-05,
     0.1819934, -4.756747e-05, 3.725371e-05, -0.111641, 8.024094e-05,
     -0.0001579762, 0.006331891, -9.018468e-06, -3.284802e-06, 0.01359519,
     -0.0001387899, 0.0006813917, 0.002476567, 4.957162e-06, -3.023798e-05,
     0.06771159, 1.517941e-05, -0.0002058754, -0.2001869, -2.10852e-05,
     0.0008199392, -0.007883554, 1.146512e-05, 2.236023e-06, -24.56835,
     0.03599721, 0.002476567, 598.7282, -0.2537373, -0.1714835, 621.5064,
     -0.1324206, -0.03202797, 708.2716, -0.2273152, -0.6334507, 96.90064,
     -0.148434, 0.1611069, 0.01068199, -1.627649e-05, 4.957162e-06,
     -0.2537373, 0.0001317226, -4.946012e-06, -0.2761304, 6.746938e-05,
     -2.509346e-05, -0.3128512, 0.0001360914, 0.0001509308, -0.03530109,
     7.383013e-05, -0.0001661873, 0.01128718, -1.099374e-05, -3.023798e-05,
     -0.1714835, -4.946012e-06, 0.0004525323, -0.1464408, 3.600144e-06,
     0.0002017756, -0.06911249, -9.216937e-05, 0.0008507719, -0.04312718,
     1.275923e-05, 0.0004036301, -151.2304, 0.1819934, 0.06771159,
     621.5064, -0.2761304, -0.1464408, 7051.173, -1.602906, 0.4053973,
     -1545.723, 0.7425596, -0.1876437, 138.2049, -0.2472585, 0.3901838,
     0.03113382, -4.756747e-05, 1.517941e-05, -0.1324206, 6.746938e-05,
     3.600144e-06, -1.602906, 0.0004067335, -0.0002464614, 0.3156405,
     -0.0001902247, 0.0002016226, -0.02968487, 6.106473e-05, -0.0001317617,
     -0.0008632869, 3.725371e-05, -0.0002058754, -0.03202797,
     -2.509346e-05, 0.0002017756, 0.4053973, -0.0002464614, 0.001022042,
     0.06312597, 0.0001262192, -0.001058175, -0.005896077, -2.681322e-05,
     0.0002789039, 123.4479, -0.111641, -0.2001869, 708.2716, -0.3128512,
     -0.06911249, -1545.723, 0.3156405, 0.06312597, 7924.038, -3.466568,
     -2.231136, 239.5488, -0.4153939, 0.8602673, -0.05306735, 8.024094e-05,
     -2.10852e-05, -0.2273152, 0.0001360914, -9.216937e-05, 0.7425596,
     -0.0001902247, 0.0001262192, -3.466568, 0.001833114, -0.000501981,
     -0.06757416, 0.0001784036, -0.000608578, 0.01009713, -0.0001579762,
     0.0008199392, -0.6334507, 0.0001509308, 0.0008507719, -0.1876437,
     0.0002016226, -0.001058175, -2.231136, -0.000501981, 0.01092386,
     -0.2434222, 0.000215744, 0.001152234, -2.477967, 0.006331891,
     -0.007883554, 96.90064, -0.03530109, -0.04312718, 138.2049,
     -0.02968487, -0.005896077, 239.5488, -0.06757416, -0.2434222,
     35.79084, -0.05138861, 0.04478089, 0.004861604, -9.018468e-06,
     1.146512e-05, -0.148434, 7.383013e-05, 1.275923e-05, -0.2472585,
     6.106473e-05, -2.681322e-05, -0.4153939, 0.0001784036, 0.000215744,
     -0.05138861, 0.0001078233, -0.0002446421, 0.002005951, -3.284802e-06,
     2.236023e-06, 0.1611069, -0.0001661873, 0.0004036301, 0.3901838,
     -0.0001317617, 0.0002789039, 0.8602673, -0.000608578, 0.001152234,
     0.04478089, -0.0002446421, 0.001393647
    ]).reshape(15,15, order='F')
RSURI.cov_params_rownames = ['Chrysler_(Intercept)', 'Chrysler_value', 'Chrysler_capital', 'General.Electric_(Intercept)', 'General.Electric_value', 'General.Electric_capital', 'General.Motors_(Intercept)', 'General.Motors_value', 'General.Motors_capital', 'US.Steel_(Intercept)', 'US.Steel_value', 'US.Steel_capital', 'Westinghouse_(Intercept)', 'Westinghouse_value', 'Westinghouse_capital', ]
RSURI.cov_params_colnames = ['Chrysler_(Intercept)', 'Chrysler_value', 'Chrysler_capital', 'General.Electric_(Intercept)', 'General.Electric_value', 'General.Electric_capital', 'General.Motors_(Intercept)', 'General.Motors_value', 'General.Motors_capital', 'US.Steel_(Intercept)', 'US.Steel_value', 'US.Steel_capital', 'Westinghouse_(Intercept)', 'Westinghouse_value', 'Westinghouse_capital', ]
RSURI.cov_resids_est = np.array([
     156.1276, 13.71096, -337.2209, 435.7109, 19.11043, 13.71096, 750.4185,
     536.9561, 1465.394, 222.2396, -337.2209, 536.9561, 7346.038,
     -2737.062, 114.6409, 435.7109, 1465.394, -2737.062, 8614.219,
     690.6026, 19.11043, 222.2396, 114.6409, 690.6026, 102.9749
    ]).reshape(5,5, order='F')
RSURI.cov_resids_est_rownames = ['Chrysler', 'General.Electric', 'General.Motors', 'US.Steel', 'Westinghouse', ]
RSURI.cov_resids_est_colnames = ['Chrysler', 'General.Electric', 'General.Motors', 'US.Steel', 'Westinghouse', ]
RSURI.cov_resids = np.array([
     156.1279, 13.71222, -337.2252, 435.7136, 19.11137, 13.71222, 750.4247,
     536.921, 1465.436, 222.2453, -337.2252, 536.921, 7346.091, -2737.188,
     114.6317, 435.7136, 1465.436, -2737.188, 8614.442, 690.6373, 19.11137,
     222.2453, 114.6317, 690.6373, 102.9786
    ]).reshape(5,5, order='F')
RSURI.cov_resids_rownames = ['Chrysler', 'General.Electric', 'General.Motors', 'US.Steel', 'Westinghouse', ]
RSURI.cov_resids_colnames = ['Chrysler', 'General.Electric', 'General.Motors', 'US.Steel', 'Westinghouse', ]
RSURI.method = 'SUR'
RSURI.rank = 15
RSURI.df_resid = 85
RSURI.iter = 11
RSURI.panelLike = '''TRUE'''
RSURI.fittedvalues = np.array([
     34.14468, 61.88879, 72.40155, 48.07059, 67.89037, 71.92845, 68.81835,
     52.25018, 62.69633, 67.97182, 75.97709, 88.31145, 71.11673, 82.85262,
     87.27159, 98.917, 118.8367, 139.9259, 175.0038, 176.1961, 39.32559,
     71.09502, 101.5503, 77.91412, 87.7393, 84.79545, 77.79214, 76.4365,
     86.04093, 83.91927, 95.48414, 105.873, 98.29794, 106.359, 108.6179,
     118.513, 128.9197, 144.757, 163.9792, 188.3904, 200.2805, 416.9796,
     547.9813, 244.9303, 432.2375, 474.9321, 482.0606, 338.0311, 423.5203,
     439.775, 521.9805, 582.8572, 551.4047, 580.1528, 673.7014, 711.3142,
     887.8988, 986.0671, 1285.158, 1379.137, 275.2061, 321.9238, 434.7202,
     382.2038, 414.095, 423.4532, 444.5821, 432.6862, 413.913, 388.9735,
     373.9205, 373.6806, 382.9809, 376.8731, 394.1132, 397.1719, 458.2386,
     473.9119, 512.2256, 534.6268, 14.94428, 32.16585, 43.683, 35.03405,
     33.03952, 38.90093, 34.32669, 36.32999, 39.99979, 40.70443, 46.61401,
     47.66481, 38.88036, 43.75353, 39.90911, 42.49191, 46.99655, 54.91891,
     73.2904, 74.18185
    ])


RSURR = Bunch()
RSURR.call = '''systemfit(formula = formula, method = "SUR", data = panel, restrict.matrix = R,      restrict.rhs = q, methodResidCov = "noDfCor", residCovRestricted = FALSE)'''
RSURR.params = np.squeeze(np.array([
     2.497993, 0.06620317, 0.3114482, -3.418123, 0.02952898, 0.1230083,
     -136.5368, 0.1152541, 0.3804054, -2.823228, 0.1537366, 0.3704575,
     3.10905, 0.05401286, 0.04309126
    ]).reshape(15,1, order='F'))
RSURR.cov_params = np.array([
     116.6885, -0.1607777, 0.008893081, -116.8489, 0.05114275, 0.02946246,
     -189.0883, 0.03981355, 0.00305605, -116.7351, 0.04779686, 0.08978693,
     -16.19571, 0.02767244, -0.0382318, -0.1607777, 0.000256699,
     -0.0001286929, 0.1611173, -7.288199e-05, -3.249216e-05, 0.2526184,
     -6.230035e-05, 2.897008e-05, 0.1607962, -3.225758e-05, -0.0002670715,
     0.02451648, -3.924989e-05, 4.619488e-05, 0.008893081, -0.0001286929,
     0.0006630121, -0.009594562, 1.415432e-05, -4.852414e-05, -0.001613841,
     2.767038e-05, -0.0001885367, -0.00864026, -0.0001207471, 0.0008504262,
     -0.01019167, 1.192106e-05, 2.355799e-05, -116.8489, 0.1611173,
     -0.009594562, 117.0214, -0.05107893, -0.03029763, 190.3932,
     -0.0401395, -0.002889117, 116.8832, -0.04615003, -0.1017246, 16.38142,
     -0.027784, 0.03678611, 0.05114275, -7.288199e-05, 1.415432e-05,
     -0.05107893, 4.719203e-05, -7.14715e-05, -0.09877716, 2.990113e-05,
     -3.735875e-05, -0.05134758, 5.023719e-05, -8.063886e-05, -0.002148651,
     2.427744e-05, -0.0001242798, 0.02946246, -3.249216e-05, -4.852414e-05,
     -0.03029763, -7.14715e-05, 0.0004391937, 0.03376507, -3.535705e-05,
     0.0001932636, -0.02854966, -8.688085e-05, 0.0007066882, -0.01988079,
     -2.943246e-05, 0.0004834217, -189.0883, 0.2526184, -0.001613841,
     190.3932, -0.09877716, 0.03376507, 7254.421, -1.686944, 0.5778943,
     192.552, -0.1259064, -0.03771701, 75.75118, -0.1580825, 0.3958046,
     0.03981355, -6.230035e-05, 2.767038e-05, -0.0401395, 2.990113e-05,
     -3.535705e-05, -1.686944, 0.0004351866, -0.0002940425, -0.04056322,
     -4.48323e-06, 0.0001438971, -0.01598111, 4.09037e-05, -0.0001274974,
     0.00305605, 2.897008e-05, -0.0001885367, -0.002889117, -3.735875e-05,
     0.0001932636, 0.5778943, -0.0002940425, 0.001076924, -0.003340983,
     0.0001404415, -0.0009211138, -0.001476289, -2.870005e-05,
     0.0002478117, -116.7351, 0.1607962, -0.00864026, 116.8832,
     -0.05134758, -0.02854966, 192.552, -0.04056322, -0.003340983,
     116.7983, -0.04986001, -0.07641557, 16.08592, -0.02777806, 0.04031809,
     0.04779686, -3.225758e-05, -0.0001207471, -0.04615003, 5.023719e-05,
     -8.688085e-05, -0.1259064, -4.48323e-06, 0.0001404415, -0.04986001,
     0.0003859509, -0.001806915, 0.0181502, 2.412733e-05, -0.0002789518,
     0.08978693, -0.0002670715, 0.0008504262, -0.1017246, -8.063886e-05,
     0.0007066882, -0.03771701, 0.0001438971, -0.0009211138, -0.07641557,
     -0.001806915, 0.01270267, -0.1337993, 1.223985e-05, 0.001575897,
     -16.19571, 0.02451648, -0.01019167, 16.38142, -0.002148651,
     -0.01988079, 75.75118, -0.01598111, -0.001476289, 16.08592, 0.0181502,
     -0.1337993, 23.74444, -0.0344561, 0.02702128, 0.02767244,
     -3.924989e-05, 1.192106e-05, -0.027784, 2.427744e-05, -2.943246e-05,
     -0.1580825, 4.09037e-05, -2.870005e-05, -0.02777806, 2.412733e-05,
     1.223985e-05, -0.0344561, 8.711157e-05, -0.0002505189, -0.0382318,
     4.619488e-05, 2.355799e-05, 0.03678611, -0.0001242798, 0.0004834217,
     0.3958046, -0.0001274974, 0.0002478117, 0.04031809, -0.0002789518,
     0.001575897, 0.02702128, -0.0002505189, 0.001599014
    ]).reshape(15,15, order='F')
RSURR.cov_params_rownames = ['Chrysler_(Intercept)', 'Chrysler_value', 'Chrysler_capital', 'General.Electric_(Intercept)', 'General.Electric_value', 'General.Electric_capital', 'General.Motors_(Intercept)', 'General.Motors_value', 'General.Motors_capital', 'US.Steel_(Intercept)', 'US.Steel_value', 'US.Steel_capital', 'Westinghouse_(Intercept)', 'Westinghouse_value', 'Westinghouse_capital', ]
RSURR.cov_params_colnames = ['Chrysler_(Intercept)', 'Chrysler_value', 'Chrysler_capital', 'General.Electric_(Intercept)', 'General.Electric_value', 'General.Electric_capital', 'General.Motors_(Intercept)', 'General.Motors_value', 'General.Motors_capital', 'US.Steel_(Intercept)', 'US.Steel_value', 'US.Steel_capital', 'Westinghouse_(Intercept)', 'Westinghouse_value', 'Westinghouse_capital', ]
RSURR.cov_resids_est = np.array([
     149.8722, -21.37565, -282.7564, 367.8402, 13.30695, -21.37565,
     660.8294, 607.5331, 978.4503, 176.4491, -282.7564, 607.5331, 7160.294,
     -1967.046, 126.1762, 367.8402, 978.4503, -1967.046, 7904.663,
     511.4995, 13.30695, 176.4491, 126.1762, 511.4995, 88.6617
    ]).reshape(5,5, order='F')
RSURR.cov_resids_est_rownames = ['Chrysler', 'General.Electric', 'General.Motors', 'US.Steel', 'Westinghouse', ]
RSURR.cov_resids_est_colnames = ['Chrysler', 'General.Electric', 'General.Motors', 'US.Steel', 'Westinghouse', ]
RSURR.cov_resids = np.array([
     154.0011, -0.3068137, -320.1221, 418.4464, 15.92695, -0.3068137,
     710.0874, 587.5187, 1275.618, 202.6887, -320.1221, 587.5187, 7188.833,
     -2181.402, 143.2504, 418.4464, 1275.618, -2181.402, 7957.594,
     604.9715, 15.92695, 202.6887, 143.2504, 604.9715, 96.62241
    ]).reshape(5,5, order='F')
RSURR.cov_resids_rownames = ['Chrysler', 'General.Electric', 'General.Motors', 'US.Steel', 'Westinghouse', ]
RSURR.cov_resids_colnames = ['Chrysler', 'General.Electric', 'General.Motors', 'US.Steel', 'Westinghouse', ]
RSURR.method = 'SUR'
RSURR.rank = 13
RSURR.df_resid = 87
RSURR.iter = 1
RSURR.restrict_matrix = np.array([
     1, 2, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 3, 1, 1, 0, 1, 0, 1, 1,
     0, 0, 0, 1, 1, 0, 0
    ]).reshape(2,15, order='F')
RSURR.restrict_matrix_rownames = ['Chrysler_((Intercept)  + General.Electric_(Intercept)  + General.Motors_value  + General.Motors_capital  + US.Steel_capital  + Westinghouse_value = 0', '2 Chrysler_((Intercept)  + Chrysler_capital  + General.Electric_(Intercept)  + 3 General.Motors_value  + General.Motors_capital  + US.Steel_(Intercept)  + US.Steel_value  + Westinghouse_value = 0', ]
RSURR.restrict_matrix_colnames = ['Chrysler_(Intercept)', 'Chrysler_value', 'Chrysler_capital', 'General.Electric_(Intercept)', 'General.Electric_value', 'General.Electric_capital', 'General.Motors_(Intercept)', 'General.Motors_value', 'General.Motors_capital', 'US.Steel_(Intercept)', 'US.Steel_value', 'US.Steel_capital', 'Westinghouse_(Intercept)', 'Westinghouse_value', 'Westinghouse_capital', ]
RSURR.restrict_rhs = np.array([
     0, 0
    ]).reshape(2,1, order='F')
RSURR.restrict_rhs_rownames = ['Chrysler_((Intercept)  + General.Electric_(Intercept)  + General.Motors_value  + General.Motors_capital  + US.Steel_capital  + Westinghouse_value = 0', '2 Chrysler_((Intercept)  + Chrysler_capital  + General.Electric_(Intercept)  + 3 General.Motors_value  + General.Motors_capital  + US.Steel_(Intercept)  + US.Steel_value  + Westinghouse_value = 0', ]
RSURR.restrict_rhs_colnames = ['*rhs*', ]
RSURR.panelLike = '''TRUE'''
RSURR.fittedvalues = np.array([
     33.40802, 61.13978, 71.82223, 47.62138, 67.52241, 71.57884, 68.52726,
     51.93828, 62.35012, 67.57691, 75.53743, 88.0812, 70.97782, 82.80431,
     87.48519, 99.23824, 119.4361, 141.1345, 176.5927, 178.2719, 43.17871,
     68.94846, 93.87545, 76.02603, 84.43639, 82.49692, 77.91351, 78.87568,
     87.59022, 85.92573, 95.18066, 104.3516, 101.6435, 110.8009, 114.9175,
     123.7739, 132.8824, 147.3096, 165.0563, 187.421, 219.338, 420.7525,
     544.0341, 264.8565, 437.9516, 477.5117, 485.0871, 352.8881, 431.1338,
     444.8852, 522.2042, 581.3111, 559.5855, 589.4667, 677.978, 714.377,
     879.9019, 975.2481, 1258.939, 1355.045, 226.5581, 293.7022, 452.373,
     370.5877, 413.9274, 430.0133, 459.9843, 441.2255, 414.1633, 379.4342,
     360.824, 364.1805, 371.4924, 360.8151, 383.5233, 387.6042, 475.8902,
     493.7127, 540.4792, 570.5019, 13.53008, 31.01416, 42.8033, 34.15781,
     32.20298, 38.19805, 33.67926, 36.04101, 40.08269, 40.88883, 46.90896,
     47.89167, 39.29956, 44.50948, 40.7521, 43.30859, 47.79249, 56.05134,
     75.10574, 76.52492
    ])




RSURIR = Bunch()
RSURIR.call = '''systemfit(formula = formula, method = "SUR", data = panel, restrict.matrix = R,      restrict.rhs = q, methodResidCov = "noDfCor", residCovRestricted = FALSE,      maxiter = 100, tol = 1e-05)'''
RSURIR.params = np.squeeze(np.array([
     3.788072, 0.06451802, 0.3093206, -4.659783, 0.0329214, 0.1086593,
     -136.9399, 0.1151543, 0.3828372, -4.170676, 0.1613182, 0.3183434,
     4.038426, 0.05537583, 0.0195867
    ]).reshape(15,1, order='F'))
RSURIR.cov_params = np.array([
     116.1575, -0.1609867, 0.01379564, -116.3625, 0.04990122, 0.03448678,
     -198.9251, 0.0419263, 0.001961945, -116.1674, 0.04085423, 0.1286802,
     -19.81814, 0.03241735, -0.03709723, -0.1609867, 0.0002591606,
     -0.000137621, 0.1613813, -6.976074e-05, -4.388515e-05, 0.2644264,
     -6.595494e-05, 3.38017e-05, 0.160961, -2.220296e-05, -0.000317525,
     0.02910747, -4.489786e-05, 4.447831e-05, 0.01379564, -0.000137621,
     0.0006758005, -0.01447052, 1.155564e-05, -2.075026e-05, -0.006634625,
     3.158313e-05, -0.0002078687, -0.01357653, -0.0001156762, 0.0008424012,
     -0.007424204, 8.760713e-06, 2.062643e-05, -116.3625, 0.1613813,
     -0.01447052, 116.5773, -0.04984426, -0.03543428, 200.3026, -0.0422736,
     -0.001759976, 116.3629, -0.03960747, -0.1382309, 20.01065,
     -0.03254706, 0.03565069, 0.04990122, -6.976074e-05, 1.155564e-05,
     -0.04984426, 4.657077e-05, -6.629991e-05, -0.102658, 3.030917e-05,
     -3.673272e-05, -0.05010295, 5.33222e-05, -7.623441e-05, -0.002403103,
     2.569573e-05, -0.0001221452, 0.03448678, -4.388515e-05, -2.075026e-05,
     -0.03543428, -6.629991e-05, 0.0004319834, 0.01939053, -3.102241e-05,
     0.0001868287, -0.0334952, -9.680353e-05, 0.0008119816, -0.02442963,
     -2.02929e-05, 0.0004733478, -198.9251, 0.2644264, -0.006634625,
     200.3026, -0.102658, 0.01939053, 6493.043, -1.502443, 0.5060838,
     201.8861, -0.1174624, -0.1679896, 105.6492, -0.2131625, 0.4867688,
     0.0419263, -6.595494e-05, 3.158313e-05, -0.0422736, 3.030917e-05,
     -3.102241e-05, -1.502443, 0.0003897633, -0.0002716213, -0.04255393,
     -7.692167e-06, 0.0001757924, -0.02211164, 5.335769e-05, -0.0001525708,
     0.001961945, 3.38017e-05, -0.0002078687, -0.001759976, -3.673272e-05,
     0.0001868287, 0.5060838, -0.0002716213, 0.001038604, -0.002291693,
     0.0001419983, -0.0009388608, -0.003690073, -3.009006e-05,
     0.0002834275, -116.1674, 0.160961, -0.01357653, 116.3629, -0.05010295,
     -0.0334952, 201.8861, -0.04255393, -0.002291693, 116.1903,
     -0.04245087, -0.1181819, 19.71516, -0.03253043, 0.03918412,
     0.04085423, -2.220296e-05, -0.0001156762, -0.03960747, 5.33222e-05,
     -9.680353e-05, -0.1174624, -7.692167e-06, 0.0001419983, -0.04245087,
     0.000319687, -0.001408009, 0.01822586, 2.693823e-05, -0.0002741997,
     0.1286802, -0.000317525, 0.0008424012, -0.1382309, -7.623441e-05,
     0.0008119816, -0.1679896, 0.0001757924, -0.0009388608, -0.1181819,
     -0.001408009, 0.01028438, -0.1363983, 2.933427e-05, 0.001528169,
     -19.81814, 0.02910747, -0.007424204, 20.01065, -0.002403103,
     -0.02442963, 105.6492, -0.02211164, -0.003690073, 19.71516,
     0.01822586, -0.1363983, 22.29315, -0.03031501, 0.01508015, 0.03241735,
     -4.489786e-05, 8.760713e-06, -0.03254706, 2.569573e-05, -2.02929e-05,
     -0.2131625, 5.335769e-05, -3.009006e-05, -0.03253043, 2.693823e-05,
     2.933427e-05, -0.03031501, 7.709927e-05, -0.0002124803, -0.03709723,
     4.447831e-05, 2.062643e-05, 0.03565069, -0.0001221452, 0.0004733478,
     0.4867688, -0.0001525708, 0.0002834275, 0.03918412, -0.0002741997,
     0.001528169, 0.01508015, -0.0002124803, 0.001432967
    ]).reshape(15,15, order='F')
RSURIR.cov_params_rownames = ['Chrysler_(Intercept)', 'Chrysler_value', 'Chrysler_capital', 'General.Electric_(Intercept)', 'General.Electric_value', 'General.Electric_capital', 'General.Motors_(Intercept)', 'General.Motors_value', 'General.Motors_capital', 'US.Steel_(Intercept)', 'US.Steel_value', 'US.Steel_capital', 'Westinghouse_(Intercept)', 'Westinghouse_value', 'Westinghouse_capital', ]
RSURIR.cov_params_colnames = ['Chrysler_(Intercept)', 'Chrysler_value', 'Chrysler_capital', 'General.Electric_(Intercept)', 'General.Electric_value', 'General.Electric_capital', 'General.Motors_(Intercept)', 'General.Motors_value', 'General.Motors_capital', 'US.Steel_(Intercept)', 'US.Steel_value', 'US.Steel_capital', 'Westinghouse_(Intercept)', 'Westinghouse_value', 'Westinghouse_capital', ]
RSURIR.cov_resids_est = np.array([
     155.6989, 11.87667, -326.8144, 425.3603, 18.0422, 11.87667, 771.7343,
     563.8665, 1452.61, 228.8926, -326.8144, 563.8665, 7205.937, -2165.033,
     143.2497, 425.3603, 1452.61, -2165.033, 8058.607, 659.5488, 18.0422,
     228.8926, 143.2497, 659.5488, 104.9542
    ]).reshape(5,5, order='F')
RSURIR.cov_resids_est_rownames = ['Chrysler', 'General.Electric', 'General.Motors', 'US.Steel', 'Westinghouse', ]
RSURIR.cov_resids_est_colnames = ['Chrysler', 'General.Electric', 'General.Motors', 'US.Steel', 'Westinghouse', ]
RSURIR.cov_resids = np.array([
     155.699, 11.87852, -326.8148, 425.3608, 18.04255, 11.87852, 771.746,
     563.8616, 1452.641, 228.8972, -326.8148, 563.8616, 7205.94, -2165.033,
     143.2494, 425.3608, 1452.641, -2165.033, 8058.63, 659.5582, 18.04255,
     228.8972, 143.2494, 659.5582, 104.9557
    ]).reshape(5,5, order='F')
RSURIR.cov_resids_rownames = ['Chrysler', 'General.Electric', 'General.Motors', 'US.Steel', 'Westinghouse', ]
RSURIR.cov_resids_colnames = ['Chrysler', 'General.Electric', 'General.Motors', 'US.Steel', 'Westinghouse', ]
RSURIR.method = 'SUR'
RSURIR.rank = 13
RSURIR.df_resid = 87
RSURIR.iter = 11
RSURIR.restrict_matrix = np.array([
     1, 2, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 3, 1, 1, 0, 1, 0, 1, 1,
     0, 0, 0, 1, 1, 0, 0
    ]).reshape(2,15, order='F')
RSURIR.restrict_matrix_rownames = ['Chrysler_((Intercept)  + General.Electric_(Intercept)  + General.Motors_value  + General.Motors_capital  + US.Steel_capital  + Westinghouse_value = 0', '2 Chrysler_((Intercept)  + Chrysler_capital  + General.Electric_(Intercept)  + 3 General.Motors_value  + General.Motors_capital  + US.Steel_(Intercept)  + US.Steel_value  + Westinghouse_value = 0', ]
RSURIR.restrict_matrix_colnames = ['Chrysler_(Intercept)', 'Chrysler_value', 'Chrysler_capital', 'General.Electric_(Intercept)', 'General.Electric_value', 'General.Electric_capital', 'General.Motors_(Intercept)', 'General.Motors_value', 'General.Motors_capital', 'US.Steel_(Intercept)', 'US.Steel_value', 'US.Steel_capital', 'Westinghouse_(Intercept)', 'Westinghouse_value', 'Westinghouse_capital', ]
RSURIR.restrict_rhs = np.array([
     0, 0
    ]).reshape(2,1, order='F')
RSURIR.restrict_rhs_rownames = ['Chrysler_((Intercept)  + General.Electric_(Intercept)  + General.Motors_value  + General.Motors_capital  + US.Steel_capital  + Westinghouse_value = 0', '2 Chrysler_((Intercept)  + Chrysler_capital  + General.Electric_(Intercept)  + 3 General.Motors_value  + General.Motors_capital  + US.Steel_(Intercept)  + US.Steel_value  + Westinghouse_value = 0', ]
RSURIR.restrict_rhs_colnames = ['*rhs*', ]
RSURIR.panelLike = '''TRUE'''
RSURIR.fittedvalues = np.array([
     33.97221, 60.99634, 71.54898, 48.06332, 67.53029, 71.4997, 68.57278,
     52.38402, 62.50589, 67.56136, 75.28503, 87.68467, 71.08624, 82.68942,
     87.46692, 99.01244, 118.9299, 140.5812, 175.4587, 177.4943, 44.50489,
     73.04721, 100.4506, 79.46258, 88.37208, 85.81106, 79.7242, 78.89154,
     87.69302, 85.79743, 96.16402, 105.6367, 99.4732, 107.2048, 109.6611,
     118.7061, 128.1804, 142.7044, 160.3766, 182.7872, 218.6347, 420.0123,
     543.4752, 264.6836, 437.6129, 477.1492, 484.8506, 352.9, 430.9686,
     444.5355, 521.9626, 581.3971, 560.6824, 590.982, 679.6864, 716.2718,
     881.9535, 977.8324, 1262.236, 1359.498, 232.7361, 303.4237, 465.1615,
     369.3415, 411.1234, 432.12, 463.0622, 440.7531, 412.1381, 377.294,
     362.362, 371.5993, 369.967, 355.8, 376.5171, 380.3277, 474.0726,
     485.5879, 522.0339, 550.2925, 14.67815, 32.62802, 44.55235, 35.42556,
     33.28861, 39.36118, 34.48982, 36.30621, 39.86951, 40.52877, 46.6713,
     47.8362, 38.41002, 43.27186, 39.14423, 41.89066, 46.65985, 54.73855,
     73.55324, 74.05651
    ])



# 2SLS tests based on sysreg/tests/results/kmenta.R
R2SLS = Bunch()
R2SLS.call = '''systemfit(formula = system, method = "2SLS", inst = inst, data = Kmenta,      methodResidCov = "noDfCor")'''
R2SLS.params = np.squeeze(np.array([
     94.6333, -0.2435565, 0.3139918, 49.53244, 0.2400758, 0.2556057,
     0.2529242
    ]).reshape(7,1, order='F'))
R2SLS.cov_params = np.array([
     53.32873, -0.5724084, 0.04190637, 0, 0, 0, 0, -0.5724084, 0.007912836,
     -0.002245614, 0, 0, 0, 0, 0.04190637, -0.002245614, 0.001873151, 0, 0,
     0, 0, 0, 0, 0, 115.4022, -0.8763283, -0.2590548, -0.236183, 0, 0, 0,
     -0.8763283, 0.00798942, 0.0007489774, 0.0004632555, 0, 0, 0,
     -0.2590548, 0.0007489774, 0.001786055, 0.001101445, 0, 0, 0,
     -0.236183, 0.0004632555, 0.001101445, 0.007944909
    ]).reshape(7,7, order='F')
R2SLS.cov_params_rownames = ['demand_(Intercept)', 'demand_price', 'demand_income', 'supply_(Intercept)', 'supply_price', 'supply_farmPrice', 'supply_trend', ]
R2SLS.cov_params_colnames = ['demand_(Intercept)', 'demand_price', 'demand_income', 'supply_(Intercept)', 'supply_price', 'supply_farmPrice', 'supply_trend', ]
R2SLS.cov_resids = np.array([
     3.286454, 3.593237, 3.593237, 4.831662
    ]).reshape(2,2, order='F')
R2SLS.cov_resids_rownames = ['demand', 'supply', ]
R2SLS.cov_resids_colnames = ['demand', 'supply', ]
R2SLS.method = '2SLS'
R2SLS.rank = 7
R2SLS.df_resid = 33
R2SLS.panelLike = '''FALSE'''
R2SLS.fittedvalues = np.array([
     97.64186, 99.88472, 99.80404, 100.0142, 102.1009, 101.9663, 102.422,
     102.9659, 101.4749, 100.328, 95.54263, 94.71564, 96.13309, 99.02829,
     103.839, 103.6555, 103.835, 102.0803, 103.6315, 106.9004, 98.91985,
     100.4001, 100.454, 100.7084, 102.6458, 102.5835, 102.5584, 104.7724,
     102.7475, 99.67725, 95.36613, 93.82181, 95.64862, 97.58861, 102.3105,
     104.0535, 102.8427, 102.7003, 102.5562, 105.6085
    ])
R2SLS.cov_resids_est = np.identity(2)

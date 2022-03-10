import glob
import numpy as np
import yt
import ytree
import math
import sys
import matplotlib.pyplot as plt
from yt.units import kpc
from matplotlib import cm
from matplotlib.lines import Line2D
from mpl_toolkits.axes_grid1 import AxesGrid
from matplotlib.colors import LogNorm
from yt.visualization.base_plot_types import get_multi_plot


mm_z = [23.277739, 22.651846, 22.06273, 21.512383, 20.992523, 20.500753, 20.034918, 19.59308, 19.177563, 18.77848, 18.398642, 18.03674, 17.69159, 17.3621, 17.047283, 16.74623, 14.926104, 14.703518, 14.489467, 14.281174, 14.080681, 13.887598, 13.699397, 13.5180025, 13.34103, 13.170327, 13.003641, 12.84083, 12.685508, 12.5318, 12.383297, 12.239772, 12.099293, 11.961762, 11.828736, 11.698413, 11.57229, 11.448649, 11.327416, 11.210012, 11.094823, 10.983224, 10.872254, 10.764706, 10.660448, 10.558022, 10.457378, 10.359763, 10.262529, 10.16944, 10.076651, 9.986596, 9.897995, 9.810811, 9.726161, 9.642826, 9.560777, 9.481082, 9.40258, 9.325245, 9.249052, 9.175011, 9.10101, 9.029084, 8.9591675, 8.88924, 8.821253, 8.754194, 8.688983, 8.623713, 8.560229, 8.497578, 8.435742, 8.374707, 8.315324, 8.256688, 8.198786, 8.141603, 8.085953, 8.030976, 7.975855, 7.9229946, 7.8699665, 7.8605347, 7.817564, 7.766547, 7.716116, 7.6662617, 7.616976, 7.56898, 7.52079, 7.473858, 7.4274397, 7.381527, 7.336112, 7.291874, 7.248103, 7.2041187, 7.165265, 7.1612663, 7.153947, 7.119519, 7.077544, 7.036001, 6.995522, 6.9554496, 6.915776, 6.876497, 6.837605, 6.7990947, 6.7615647, 6.7243934, 6.686986, 6.651109, 6.6149864, 6.579202, 6.5437536, 6.509199, 6.474959, 6.4404764, 6.4074073, 6.3740873, 6.3410664, 6.3083386, 6.2764316, 6.2442765, 6.2129254, 6.181844, 6.1510296, 6.120478, 6.0901875, 6.0606513, 6.030865, 6.0018206, 5.9998603]
mm_pos = [[13623.54, 13553.191, 12954.65], [13629.83, 13551.641, 12967.99], [13636.011, 13549.74, 12981.77], [13642.01, 13547.761, 12995.5], [13648.311, 13545.971, 13009.44], [13654.51, 13543.931, 13023.361], [13660.93, 13541.801, 13037.33], [13667.0, 13539.61, 13050.42], [13673.15, 13537.61, 13063.84], [13678.841, 13535.691, 13076.75], [13684.681, 13533.721, 13089.771], [13690.621, 13531.531, 13102.711], [13696.391, 13529.24, 13115.181], [13701.841, 13526.931, 13127.73], [13707.49, 13524.71, 13140.13], [13713.36, 13522.421, 13152.55], [13755.319, 13509.17, 13236.05], [13761.08, 13506.501, 13247.74], [13766.971, 13502.78, 13257.761], [13772.471, 13500.331, 13269.911], [13780.2295, 13498.311, 13280.421], [13784.54, 13494.991, 13290.511], [13790.74, 13493.07, 13300.541], [13796.051, 13491.951, 13310.32], [13801.091, 13489.75, 13320.221], [13806.95, 13487.26, 13330.19], [13814.241, 13485.989, 13341.35], [13823.82, 13485.211, 13351.961], [13826.5205, 13483.1, 13361.91], [13832.671, 13481.23, 13372.171], [13838.931, 13478.541, 13382.631], [13846.051, 13475.251, 13392.411], [13852.98, 13474.09, 13402.551], [13858.491, 13470.9795, 13412.28], [13865.7, 13469.341, 13422.011], [13872.461, 13466.791, 13431.561], [13879.49, 13464.521, 13440.9], [13885.67, 13460.931, 13450.32], [13892.19, 13458.48, 13459.66], [13900.111, 13455.61, 13469.25], [13906.82, 13452.51, 13478.66], [13913.761, 13449.661, 13488.101], [13920.931, 13446.34, 13497.812], [13928.561, 13442.951, 13507.24], [13936.41, 13439.4795, 13516.511], [13945.15, 13435.641, 13526.001], [13954.681, 13431.301, 13535.661], [13965.61, 13425.561, 13545.21], [13976.58, 13420.11, 13554.31], [13987.461, 13413.63, 13559.34], [13989.951, 13412.341, 13569.641], [14010.7705, 13399.971, 13575.631], [14017.951, 13395.591, 13581.94], [14024.551, 13391.791, 13588.26], [14030.49, 13388.251, 13594.931], [14035.04, 13386.091, 13601.961], [14039.61, 13383.891, 13609.041], [14043.721, 13382.301, 13615.891], [14047.261, 13381.11, 13622.63], [14050.471, 13380.32, 13629.811], [14053.251, 13379.811, 13636.72], [14055.61, 13379.69, 13643.851], [14057.58, 13380.09, 13650.57], [14059.201, 13380.391, 13657.481], [14060.551, 13381.67, 13664.5205], [14061.851, 13383.24, 13671.37], [14062.69, 13385.311, 13678.03], [14063.091, 13388.02, 13684.891], [14063.48, 13390.971, 13691.75], [14063.51, 13394.431, 13698.54], [14063.341, 13398.57, 13705.301], [14062.801, 13403.091, 13711.931], [14062.15, 13408.52, 13718.95], [14060.71, 13414.791, 13725.501], [14059.141, 13422.069, 13732.181], [14056.74, 13430.79, 13738.561], [14054.401, 13440.61, 13745.941], [14060.48, 13454.53, 13755.101], [14065.051, 13457.88, 13762.201], [14068.12, 13459.65, 13768.87], [14071.37, 13461.111, 13776.77], [14074.011, 13462.65, 13784.69], [14074.63, 13462.341, 13793.841], [14076.491, 13463.19, 13793.95], [14076.78, 13463.51, 13801.501], [14078.891, 13463.92, 13809.97], [14080.061, 13465.001, 13818.851], [14081.649, 13465.19, 13827.35], [14081.311, 13465.0205, 13837.9], [14083.83, 13465.221, 13844.591], [14083.7705, 13465.689, 13854.701], [14083.761, 13465.99, 13864.15], [14083.26, 13466.2, 13874.171], [14084.341, 13465.63, 13883.23], [14084.5, 13464.9, 13892.239], [14095.529, 13471.301, 13893.671], [14086.5205, 13462.2295, 13909.69], [14088.23, 13461.301, 13918.081], [14090.03, 13460.871, 13925.211], [14089.62, 13460.101, 13927.05], [14090.2705, 13460.37, 13927.46], [14091.12, 13459.201, 13933.91], [14092.79, 13459.2705, 13941.631], [14096.82, 13469.4, 13951.101], [14096.061, 13460.671, 13955.5205], [14097.98, 13460.95, 13962.551], [14099.57, 13462.86, 13969.17], [14100.701, 13465.3, 13977.101], [14100.971, 13467.359, 13986.69], [14106.56, 13470.58, 13990.44], [14100.811, 13473.12, 14004.44], [14101.76, 13476.941, 14013.331], [14099.701, 13475.82, 14022.55], [14093.11, 13466.39, 14031.551], [14098.32, 13475.881, 14040.471], [14097.561, 13474.46, 14049.63], [14097.2705, 13473.07, 14058.57], [14097.32, 13473.2, 14068.0205], [14098.49, 13473.69, 14076.601], [14099.961, 13473.541, 14085.07], [14101.261, 13474.58, 14094.291], [14103.051, 13475.791, 14102.67], [14104.761, 13477.45, 14111.6], [14106.37, 13478.871, 14120.58], [14108.17, 13480.78, 14129.58], [14109.53, 13482.2705, 14138.312], [14110.84, 13483.36, 14147.32], [14112.44, 13485.551, 14156.221], [14113.81, 13487.03, 14165.45], [14115.501, 13488.15, 14174.031], [14116.291, 13491.79, 14183.391], [14118.82, 13493.91, 14191.7], [14121.15, 13496.62, 14201.341], [14123.01, 13498.761, 14210.331], [14123.091, 13498.95, 14210.92]]
mm_rad = [2.144, 2.503, 2.819, 3.153, 3.699, 4.127, 4.482, 4.761, 4.975, 5.178, 5.397, 5.599, 5.889, 6.203, 6.61, 7.181, 10.502, 10.89, 11.65, 11.847, 12.179, 12.394, 12.615, 12.882, 13.11, 13.25, 13.518, 13.787, 13.84, 14.065, 14.119, 14.429, 14.831, 14.867, 15.156, 15.271, 15.416, 15.239, 15.26, 15.09, 15.133, 15.755, 15.747, 15.782, 15.365, 15.185, 14.208, 14.417, 13.588, 13.218, 12.826, 12.762, 12.697, 12.631, 10.983, 10.736, 9.918, 8.953, 9.865, 8.872, 8.5, 8.306, 8.364, 8.236, 7.937, 7.578, 7.954, 7.575, 7.652, 7.536, 7.275, 7.275, 7.105, 7.057, 6.857, 6.704, 6.121, 110.873, 112.791, 114.544, 116.388, 118.305, 119.873, 120.26, 121.433, 122.736, 123.945, 125.158, 126.426, 128.009, 129.556, 131.374, 133.389, 135.423, 137.193, 138.66, 139.829, 141.142, 142.261, 142.338, 142.58, 143.469, 144.482, 145.494, 146.655, 147.796, 148.864, 149.764, 150.541, 151.296, 152.195, 153.334, 154.268, 155.038, 156.354, 157.323, 158.194, 159.039, 159.905, 160.785, 161.786, 162.846, 163.89, 164.854, 165.74, 166.656, 167.603, 168.395, 169.152, 169.809, 170.469, 171.037, 171.589, 172.086, 172.115]

mm_parent_rvir = [57.589, 55.892, 57.262, 58.569, 48.407, 70.997, 71.542, 72.224, 72.873, 73.061, 74.229, 74.832, 75.523, 76.604, 77.963, 78.925, 79.638, 80.23, 80.859, 81.708, 82.691, 84.316, 86.731, 91.304, 95.183, 97.756, 74.174, 74.983, 71.484, 15.984, 15.976, 67.532, 67.982, 59.655]
mm_parent_pos =[[13971.651, 13416.761, 13500.491], [13973.251, 13417.82, 13508.961], [13975.28, 13418.161, 13518.0], [13978.311, 13417.6, 13528.051], [13981.591, 13415.83, 13538.461], [13984.431, 13417.091, 13547.311], [13985.671, 13419.811, 13554.94], [13987.791, 13421.03, 13563.791], [13990.811, 13421.511, 13573.261], [13993.861, 13427.38, 13581.311], [13995.671, 13415.69, 13595.351], [13998.25, 13418.63, 13603.921], [13998.73, 13417.351, 13613.24], [14002.11, 13420.181, 13618.439], [14005.36, 13424.61, 13627.101], [14007.561, 13424.28, 13634.56], [14009.461, 13424.35, 13642.201], [14012.421, 13425.71, 13649.841], [14014.351, 13426.171, 13657.091], [14018.0, 13429.921, 13663.2705], [14020.501, 13431.86, 13670.5], [14022.961, 13434.081, 13677.33], [14025.271, 13435.041, 13684.701], [14027.73, 13436.07, 13692.15], [14030.011, 13439.03, 13698.711], [14032.31, 13439.63, 13705.49], [14067.5205, 13458.5205, 13662.58], [14067.12, 13458.87, 13675.38], [14066.95, 13459.74, 13689.58], [14062.75, 13420.21, 13714.62], [14070.35, 13424.73, 13728.721], [14063.431, 13459.73, 13731.001], [14059.801, 13457.91, 13745.261], [14055.24, 13455.431, 13758.3]]

mm_merger_z=[21.512383, 20.992523, 20.500753, 20.034918, 19.59308, 19.177563, 18.77848, 18.398642, 18.03674, 17.69159, 17.3621, 17.047283, 16.74623, 14.926104, 14.703518, 14.489467, 14.281174, 14.080681, 13.887598, 13.699397, 13.5180025, 13.34103, 13.170327, 13.003641, 12.84083, 12.685508, 12.5318, 12.383297, 12.239772, 12.099293, 11.961762, 11.828736, 11.698413, 11.57229, 11.448649, 11.327416, 11.210012, 11.094823, 10.983224, 10.872254, 10.764706, 10.660448, 10.558022, 10.457378, 10.359763, 10.262529, 10.16944, 10.076651, 9.986596, 9.897995, 9.810811, 9.726161, 9.642826, 9.560777, 9.481082, 9.40258, 9.325245, 9.249052, 9.175011, 9.10101, 9.029084, 8.9591675, 8.88924, 8.821253, 8.754194, 8.688983, 8.623713, 8.560229, 8.497578, 8.435742, 8.374707, 8.315324, 8.256688, 8.198786, 8.141603, 8.085953, 8.030976, 7.975855, 7.9229946, 7.8699665, 7.8605347, 7.817564, 7.766547, 7.716116, 7.6662617, 7.616976, 7.56898, 7.52079, 7.473858, 7.4274397, 7.381527, 7.336112, 7.291874, 7.248103, 7.2041187, 7.165265, 7.1612663, 7.153947, 7.119519, 7.077544, 7.036001, 6.995522, 6.9554496, 6.915776, 6.876497, 6.837605, 6.7990947, 6.7615647, 6.7243934, 6.686986, 6.651109, 6.6149864, 6.579202, 6.5437536, 6.509199, 6.474959, 6.4404764, 6.4074073, 6.3740873, 6.3410664, 6.3083386, 6.2764316, 6.2442765, 6.2129254, 6.181844, 6.1510296, 6.120478, 6.0901875, 6.0606513, 6.030865, 6.0018206, 5.9998603]
mm_merger_rad=[2.979, 3.364, 3.905, 4.119, 4.429, 4.858, 5.144, 5.468, 5.788, 6.093, 6.336, 6.701, 7.193, 7.576, 22.92, 23.973, 24.927, 25.884, 26.874, 27.91, 28.73, 29.682, 30.931, 29.85, 29.758, 29.504, 29.945, 31.983, 32.046, 29.384, 32.796, 27.411, 30.38, 30.864, 38.549, 37.241, 35.834, 32.214, 37.629, 35.338, 67.684, 68.519, 69.202, 69.538, 70.503, 70.997, 71.542, 72.224, 72.873, 73.061, 74.229, 74.832, 75.523, 76.604, 77.963, 78.925, 79.638, 80.23, 80.859, 81.708, 82.691, 84.316, 86.731, 91.304, 95.183, 97.756, 100.692, 102.174, 103.527, 104.66, 105.69, 106.822, 107.838, 109.142, 110.873, 112.791, 114.544, 116.388, 118.305, 119.873, 120.26, 121.433, 122.736, 123.945, 125.158, 126.426, 128.009, 129.556, 131.374, 133.389, 135.423, 137.193, 138.66, 139.829, 141.142, 142.261, 142.338, 142.58, 143.469, 144.482, 145.494, 146.655, 147.796, 148.864, 149.764, 150.541, 151.296, 152.195, 153.334, 154.268, 155.038, 156.354, 157.323, 158.194, 159.039, 159.905, 160.785, 161.786, 162.846, 163.89, 164.854, 165.74, 166.656, 167.603, 168.395, 169.152, 169.809, 170.469, 171.037, 171.589, 172.086, 172.115]
mm_merger_pos=[[13976.95, 13373.77, 13066.069], [13976.29, 13374.94, 13077.461], [13977.131, 13375.41, 13087.44], [13977.2, 13375.71, 13097.01], [13977.26, 13376.47, 13106.79], [13977.17, 13377.32, 13116.5205], [13977.131, 13378.011, 13126.501], [13977.07, 13378.44, 13136.011], [13977.44, 13379.131, 13145.45], [13977.121, 13379.72, 13154.751], [13976.74, 13380.29, 13163.71], [13976.16, 13380.841, 13172.7705], [13975.98, 13381.42, 13181.431], [13973.68, 13378.341, 13237.34], [13973.35, 13379.171, 13251.24], [13972.961, 13380.821, 13261.801], [13971.961, 13381.561, 13272.251], [13970.82, 13382.391, 13282.2], [13969.41, 13383.63, 13292.16], [13967.99, 13384.95, 13302.37], [13966.48, 13385.721, 13312.472], [13963.86, 13386.4, 13322.43], [13959.931, 13387.262, 13332.561], [13955.78, 13388.631, 13343.2705], [13951.431, 13390.32, 13354.091], [13947.141, 13392.391, 13364.96], [13942.741, 13394.551, 13375.68], [13938.601, 13398.551, 13385.621], [13937.26, 13403.061, 13396.15], [13937.62, 13407.071, 13406.54], [13939.6, 13409.851, 13417.031], [13941.32, 13410.671, 13427.971], [13943.54, 13410.28, 13438.921], [13946.351, 13408.87, 13449.2], [13948.811, 13406.081, 13459.37], [13961.871, 13391.551, 13467.351], [13965.01, 13399.74, 13472.0205], [13966.44, 13406.03, 13478.24], [13968.08, 13411.73, 13484.811], [13969.55, 13415.681, 13492.06], [13969.95, 13400.71, 13512.141], [13973.751, 13403.061, 13518.92], [13977.36, 13406.291, 13526.09], [13982.661, 13388.751, 13540.391], [13983.051, 13413.48, 13540.029], [13984.431, 13417.091, 13547.311], [13985.671, 13419.811, 13554.94], [13987.791, 13421.03, 13563.791], [13990.811, 13421.511, 13573.261], [13993.861, 13427.38, 13581.311], [13995.671, 13415.69, 13595.351], [13998.25, 13418.63, 13603.921], [13998.73, 13417.351, 13613.24], [14002.11, 13420.181, 13618.439], [14005.36, 13424.61, 13627.101], [14007.561, 13424.28, 13634.56], [14009.461, 13424.35, 13642.201], [14012.421, 13425.71, 13649.841], [14014.351, 13426.171, 13657.091], [14018.0, 13429.921, 13663.2705], [14020.501, 13431.86, 13670.5], [14022.961, 13434.081, 13677.33], [14025.271, 13435.041, 13684.701], [14027.73, 13436.07, 13692.15], [14030.011, 13439.03, 13698.711], [14032.31, 13439.63, 13705.49], [14035.841, 13442.47, 13710.721], [14036.661, 13441.701, 13718.84], [14039.051, 13443.33, 13725.011], [14041.03, 13443.97, 13730.07], [14044.92, 13445.851, 13734.581], [14046.291, 13446.79, 13739.95], [14051.02, 13449.24, 13743.561], [14054.561, 13451.53, 13749.221], [14060.48, 13454.53, 13755.101], [14065.051, 13457.88, 13762.201], [14068.12, 13459.65, 13768.87], [14071.37, 13461.111, 13776.77], [14074.011, 13462.65, 13784.69], [14074.63, 13462.341, 13793.841], [14076.491, 13463.19, 13793.95], [14076.78, 13463.51, 13801.501], [14078.891, 13463.92, 13809.97], [14080.061, 13465.001, 13818.851], [14081.649, 13465.19, 13827.35], [14081.311, 13465.0205, 13837.9], [14083.83, 13465.221, 13844.591], [14083.7705, 13465.689, 13854.701], [14083.761, 13465.99, 13864.15], [14083.26, 13466.2, 13874.171], [14084.341, 13465.63, 13883.23], [14084.5, 13464.9, 13892.239], [14095.529, 13471.301, 13893.671], [14086.5205, 13462.2295, 13909.69], [14088.23, 13461.301, 13918.081], [14090.03, 13460.871, 13925.211], [14089.62, 13460.101, 13927.05], [14090.2705, 13460.37, 13927.46], [14091.12, 13459.201, 13933.91], [14092.79, 13459.2705, 13941.631], [14096.82, 13469.4, 13951.101], [14096.061, 13460.671, 13955.5205], [14097.98, 13460.95, 13962.551], [14099.57, 13462.86, 13969.17], [14100.701, 13465.3, 13977.101], [14100.971, 13467.359, 13986.69], [14106.56, 13470.58, 13990.44], [14100.811, 13473.12, 14004.44], [14101.76, 13476.941, 14013.331], [14099.701, 13475.82, 14022.55], [14093.11, 13466.39, 14031.551], [14098.32, 13475.881, 14040.471], [14097.561, 13474.46, 14049.63], [14097.2705, 13473.07, 14058.57], [14097.32, 13473.2, 14068.0205], [14098.49, 13473.69, 14076.601], [14099.961, 13473.541, 14085.07], [14101.261, 13474.58, 14094.291], [14103.051, 13475.791, 14102.67], [14104.761, 13477.45, 14111.6], [14106.37, 13478.871, 14120.58], [14108.17, 13480.78, 14129.58], [14109.53, 13482.2705, 14138.312], [14110.84, 13483.36, 14147.32], [14112.44, 13485.551, 14156.221], [14113.81, 13487.03, 14165.45], [14115.501, 13488.15, 14174.031], [14116.291, 13491.79, 14183.391], [14118.82, 13493.91, 14191.7], [14121.15, 13496.62, 14201.341], [14123.01, 13498.761, 14210.331], [14123.091, 13498.95, 14210.92]]

yt.enable_parallelism()


file_list = glob.glob("DD0???\\"+"output_0???", recursive=True)
for file in file_list:
    ds = yt.load(file)
    redshift = ds.current_redshift
    print("Working on redshift: "+str(redshift))

    i = np.where(np.abs(np.array(mm_z)-redshift) < 0.01)[0][0]
    print("i="+str(i))
    j = np.where(np.abs(np.array(mm_merger_z)-redshift) < 0.01)[0][0]
    print("j="+str(j))


    c=ds.arr(mm_merger_pos[j], 'kpccm/h')
    radius = 90
    width = ds.quan(2*radius, 'kpccm/h')
    field = ('deposit', 'all_cic')
    region =  ds.region(c,c-0.5*width,c+0.5*width)

    slc = []
    print("loading z projection")
    slc.append(yt.ProjectionPlot(ds, 'z', field, center=c, width=width, data_source=region,weight_field=field))
    print("loading x projection")
    slc.append(yt.ProjectionPlot(ds, 'x', field, center=c, width=width, data_source=region,weight_field=field))
    print("loading y projection")
    slc.append(yt.ProjectionPlot(ds, 'y', field, center=c, width=width, data_source=region,weight_field=field))

    slc_frbs = [s.data_source.to_frb((radius*2, "kpccm/h"), 800) for s in slc]
    slc_arrs = [np.array(slc_frb[field])[::][::-1] for slc_frb in slc_frbs]



    orient = "horizontal"
    fig, axes, colorbars = get_multi_plot(3,1, colorbar=orient)
    for y in range(3):
        axes[0][y].xaxis.set_visible(False)
        axes[0][y].yaxis.set_visible(False)

    axes[0][0].xaxis.set_visible(True)
    axes[0][1].xaxis.set_visible(True)
    axes[0][2].xaxis.set_visible(True)
    axes[0][0].set_ylabel("Kpccm/h")
    axes[0][0].yaxis.set_visible(True)
    axes[0][0].set_xlabel("Kpccm/h\nZ Projection")
    axes[0][1].set_xlabel("Kpccm/h\nX Projection")
    axes[0][2].set_xlabel("Kpccm/h\nY Projection")
    axes[0][1].set_title("Redshift "+str('%.3f'%(redshift)))

    mm_x,mm_y, mm_px, mm_py, = [],[],[],[]
    for a in np.linspace(0, 2*np.pi, 1000) :
        mm_x.append(mm_rad[i]*np.cos(a))
        mm_y.append(mm_rad[i]*np.sin(a))
        mm_px.append(mm_merger_rad[j]*np.cos(a))
        mm_py.append(mm_merger_rad[j]*np.sin(a))


    plots = []
    for y in range(3):

        plots.append(axes[0][y].imshow(slc_arrs[y],extent=[-radius,radius,-radius,radius], norm=LogNorm()))

        filt = np.where((np.abs(mm_px)<0.9*radius) & (np.abs(mm_py) <0.9*radius))
        axes[0][y].scatter(np.array(mm_px)[filt], np.array(mm_py)[filt],s=10, c="tab:green", label=r"$r_{vir}$ MMH-Parent")

        if(y==0): a,b = 0,1
        elif(y==1): a,b = 1,2
        else: a,b = 2,0
        dp = (np.array(mm_pos[i])-np.array(mm_merger_pos[j]))
        filt = np.where((np.abs(mm_x+dp[a]) <0.9*radius) & (np.abs(mm_y+dp[b]) <0.9*radius))
        axes[0][y].scatter(np.array(mm_x+dp[a])[filt], np.array(mm_y+dp[b])[filt],s=10, c="tab:orange", label=r"$r_{vir}}$ MMH")

        axes[0][y].legend(loc="upper left")
        plots[-1].set_cmap("bone")
        plots[-1].set_clim(1e-25,1e-21)

    for x in range(3):
        axes[0][x].set_xticks(np.arange(-radius+20,radius-15,20))

    t = r"$\mathrm{Density-Weighted \ Projected \ Density}\ (\mathrm{g\ cm^{-2}})$"
    k=0
    for p, cax in zip(plots[0:3:1], colorbars):
        if(k==1):
            cbar = fig.colorbar(p, cax=cax, orientation=orient)
            cbar.set_label(t)
        else:
            fig.colorbar(p, cax=cax, orientation=orient).remove()
        k+=1
    fig.savefig("figures/DD"+file.split("_")[-1]+"_collision.pdf",bbox_inches='tight')

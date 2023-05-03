
import torch
import torch.nn as nn
import numpy as np

# Définir les dimensions d'entrée et de sortie de la couche linéaire
input_dim = 100
output_dim = 50

# Définir le dictionnaire sub_obs
'''
sub_obs = {
                'p_node_id': 50,
                'hidden_state': np.squeeze(hidden_state.cpu().detach().numpy(), axis=0),
                'p_net_x': sub_obs['p_net_x'],
                'p_net_edge_index': sub_obs['p_net_edge_index'],
                'encoder_outputs': encoder_outputs,
            }'''
sub_obs={'p_node_id': 24, 'p_net_x': np.array([[0.22680412, 0.5154639 , 0.3994778 , 0.61749345, 0.        ],
       [0.11340206, 0.62886596, 0.35900784, 0.80809397, 0.        ],
       [0.0927835 , 0.5154639 , 0.08746736, 0.15796344, 0.        ],
       [0.8041237 , 0.8041237 , 0.24804178, 0.37597913, 0.        ],
       [0.7010309 , 0.7010309 , 0.11618799, 0.11618799, 0.        ],
       [0.05154639, 0.6082474 , 0.18668407, 0.37597913, 0.        ],
       [0.9484536 , 0.9484536 , 0.08093995, 0.18276763, 0.        ],
       [0.13402061, 0.814433  , 0.17493473, 0.32637075, 0.        ],
       [0.6597938 , 0.6597938 , 0.09530026, 0.15796344, 0.        ],
       [0.5051546 , 0.5154639 , 0.0770235 , 0.08746736, 0.        ],
       [0.07216495, 0.83505154, 0.27284595, 0.65143603, 0.        ],
       [0.40206185, 0.6494845 , 0.47911227, 0.8694517 , 0.        ],
       [0.97938144, 0.97938144, 0.46344647, 0.74804175, 0.        ],
       [0.        , 0.9484536 , 0.54177547, 1.        , 0.        ],
       [0.29896906, 0.7938144 , 0.11227154, 0.19843341, 0.        ],
       [0.5670103 , 0.9072165 , 0.31853786, 0.68015665, 0.        ],
       [0.10309278, 0.7525773 , 0.09921671, 0.34725848, 0.        ],
       [0.10309278, 0.814433  , 0.4464752 , 0.8067885 , 0.        ],
       [0.78350514, 0.8041237 , 0.38903394, 0.5143603 , 0.        ],
       [0.9896907 , 0.9896907 , 0.11618799, 0.18146214, 0.        ],
       [0.45360824, 0.83505154, 0.23759791, 0.25195822, 0.        ],
       [0.53608245, 0.9484536 , 0.24804178, 0.40339425, 0.        ],
       [0.5463917 , 0.91752577, 0.14490862, 0.20234987, 0.        ],
       [0.6597938 , 0.7010309 , 0.2845953 , 0.4073107 , 0.        ],
       [0.58762884, 0.73195875, 0.24281985, 0.4530026 , 0.        ],
       [0.6597938 , 0.6597938 , 0.37467363, 0.68015665, 0.        ],
       [0.58762884, 0.58762884, 0.06788512, 0.06788512, 0.        ],
       [0.6701031 , 0.7628866 , 0.3929504 , 0.7532637 , 0.        ],
       [0.8041237 , 0.8041237 , 0.07571802, 0.07571802, 0.        ],
       [0.24742268, 0.5979381 , 0.25587466, 0.38772845, 0.        ],
       [0.20618556, 0.82474226, 0.4464752 , 0.71932113, 0.        ],
       [0.30927834, 1.        , 0.26631853, 0.44125327, 0.        ],
       [0.8041237 , 0.97938144, 0.14882506, 0.1997389 , 0.        ],
       [0.13402061, 0.58762884, 0.24934725, 0.49738905, 0.        ],
       [0.21649484, 0.6597938 , 0.4086162 , 0.5992167 , 0.        ],
       [0.06185567, 0.91752577, 0.3994778 , 0.8629243 , 0.        ],
       [0.24742268, 0.556701  , 0.21409921, 0.28981724, 0.        ],
       [0.0927835 , 0.53608245, 0.38642296, 0.4086162 , 0.        ],
       [0.07216495, 0.7628866 , 0.11879896, 0.21018277, 0.        ],
       [0.0927835 , 0.96907216, 0.37336814, 0.55744123, 0.        ],
       [0.77319586, 0.77319586, 0.32898173, 0.4673629 , 0.        ],
       [0.41237113, 0.63917524, 0.12532637, 0.308094  , 0.        ],
       [0.63917524, 0.63917524, 0.43472585, 0.502611  , 0.        ],
       [0.04123711, 0.58762884, 0.4464752 , 0.72062665, 0.        ],
       [0.01030928, 0.7525773 , 0.4373368 , 0.72062665, 0.        ],
       [0.73195875, 0.88659793, 0.23368146, 0.28198433, 0.        ],
       [0.26804122, 0.83505154, 0.14751959, 0.34073108, 0.        ],
       [0.12371134, 0.5670103 , 0.18276763, 0.28198433, 0.        ],
       [0.34020618, 0.7938144 , 0.15143603, 0.24543081, 0.        ],
       [0.91752577, 0.91752577, 0.4843342 , 0.5548303 , 0.        ]],
      dtype=float), 'p_net_edge_index': np.array([[ 0,  0,  0,  0,  0,  0,  1,  1,  1,  1,  1,  1,  1,  1,  2,  2,
         3,  3,  3,  3,  4,  5,  5,  6,  6,  7,  7,  7,  8,  8,  9, 10,
        10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12,
        12, 12, 13, 13, 13, 13, 13, 13, 13, 13, 15, 15, 15, 15, 15, 15,
        16, 16, 17, 17, 17, 17, 17, 18, 18, 19, 20, 20, 21, 21, 21, 21,
        23, 23, 23, 23, 24, 24, 24, 25, 25, 25, 26, 27, 27, 27, 30, 30,
        31, 31, 32, 33, 33, 34, 34, 34, 35, 35, 36, 40, 40, 41, 41, 42,
        43,  1, 14, 27, 36, 37, 49,  5, 12, 14, 25, 27, 31, 34, 35, 33,
        42,  5, 17, 44, 46, 43, 10, 49, 32, 35, 11, 29, 35, 27, 39, 36,
        25, 35, 39, 43, 44, 48, 13, 22, 31, 38, 42, 43, 44, 13, 15, 17,
        18, 30, 38, 16, 17, 19, 27, 28, 29, 34, 48, 18, 25, 30, 34, 39,
        47, 18, 30, 24, 30, 33, 41, 45, 20, 45, 29, 31, 47, 22, 27, 35,
        44, 25, 29, 44, 48, 33, 40, 49, 37, 40, 46, 49, 30, 40, 44, 35,
        43, 37, 47, 39, 35, 42, 37, 43, 46, 39, 44, 39, 42, 49, 43, 45,
        49, 46],
       [ 1, 14, 27, 36, 37, 49,  5, 12, 14, 25, 27, 31, 34, 35, 33, 42,
         5, 17, 44, 46, 43, 10, 49, 32, 35, 11, 29, 35, 27, 39, 36, 25,
        35, 39, 43, 44, 48, 13, 22, 31, 38, 42, 43, 44, 13, 15, 17, 18,
        30, 38, 16, 17, 19, 27, 28, 29, 34, 48, 18, 25, 30, 34, 39, 47,
        18, 30, 24, 30, 33, 41, 45, 20, 45, 29, 31, 47, 22, 27, 35, 44,
        25, 29, 44, 48, 33, 40, 49, 37, 40, 46, 49, 30, 40, 44, 35, 43,
        37, 47, 39, 35, 42, 37, 43, 46, 39, 44, 39, 42, 49, 43, 45, 49,
        46,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,  1,  1,  1,  1,  2,
         2,  3,  3,  3,  3,  4,  5,  5,  6,  6,  7,  7,  7,  8,  8,  9,
        10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 12, 12, 12,
        12, 12, 12, 13, 13, 13, 13, 13, 13, 13, 13, 15, 15, 15, 15, 15,
        15, 16, 16, 17, 17, 17, 17, 17, 18, 18, 19, 20, 20, 21, 21, 21,
        21, 23, 23, 23, 23, 24, 24, 24, 25, 25, 25, 26, 27, 27, 27, 30,
        30, 31, 31, 32, 33, 33, 34, 34, 34, 35, 35, 36, 40, 40, 41, 41,
        42, 43]]), 'v_net_x': np.array([[0.5154639 , 0.02219321],
       [0.5051546 , 0.03394256],
       [0.0927835 , 0.05613577]], dtype=float)}
# Convertir le dictionnaire en un tenseur PyTorch


print(sub_obs['p_node_id'])
print(len(sub_obs['p_net_x']))
print(len(sub_obs['p_net_edge_index']))
print(len(sub_obs['v_net_x']))

print("lol")
print(sub_obs['p_node_id'])
print(len(sub_obs['p_net_x']))
print(len(sub_obs['p_net_edge_index'][0]))
print(len(sub_obs['v_net_x'][0]))

sub_obs['p_net_x']

print(torch.from_numpy(np.array([sub_obs['p_node_id']])).float().size())
print(torch.from_numpy(sub_obs['p_net_x']).float().size())
print(torch.from_numpy(sub_obs['p_net_edge_index'][0]).float().size())
print(torch.from_numpy(sub_obs['v_net_x'][0]).float().size())

t1=torch.tensor(np.array([sub_obs['p_node_id']])).resize_(50,)
print("rania_dania")
t2=torch.tensor(sub_obs['p_net_x']).resize_(50,)
t3=torch.cat([torch.tensor(sub_obs['p_net_edge_index'][0]).resize_(50,),torch.tensor(sub_obs['p_net_edge_index'][1]).resize_(50,)])
t4=torch.cat([torch.tensor(sub_obs['v_net_x'][0]).resize_(50,),torch.tensor(sub_obs['v_net_x'][1]).resize_(50,),torch.tensor(sub_obs['v_net_x'][2]).resize_(50,)])

print(t1.size())
print(t2.size())
print(t3.size())
print(t4.size())

tensor_obs = torch.cat([t1, t2, t3, t4], dim=0)

print(t1)
print(t2)
print(t3)
print(t4)

f=open("test27.txt","w")
f.write(str(t1))
f.write("\n\n\n")
f.write(str(t2))
f.write("\n\n\n")

f.write(str(t3))
f.write("\n\n\n")

f.write(str(t4))
f.write("\n\n\n tensor_obs\n")
f.write(str(tensor_obs))
f.write("\n\n\n tensor_obs size \n")
f.write(str(tensor_obs.size()))
f.close()



'''
tensor_obs = torch.cat([
    torch.from_numpy(np.array([sub_obs['p_node_id']])).float(),
    torch.from_numpy(sub_obs['p_net_x']).float(),
    torch.cat([torch.from_numpy(sub_obs['p_net_edge_index'][0]).float(),torch.from_numpy(sub_obs['p_net_edge_index'][1]).float()]),
    torch.cat([torch.from_numpy(sub_obs['v_net_x'][0]).float(),torch.from_numpy(sub_obs['v_net_x'][1]).float(),torch.from_numpy(sub_obs['v_net_x'][2]).float()])
], dim=1)
'''

'''
# Définir la couche linéaire
linear_layer = nn.Linear(input_dim, output_dim)

# Passer le tenseur à travers la couche linéaire
output = linear_layer(tensor_obs)

# Afficher la forme de sortie
print(output.shape)'''



addpath('./mesh_tools/toolbox_graph')
addpath('./mesh_tools/toolbox_general')

% data file of the model
filename = 'model2017-1_bfm_nomouth.h5';

%% display data fields of model by
% datafield = h5disp(filename)

%% load shape data (mean shape, pca shape, noise variance)
mean_shape = h5read(filename, '/shape/model/mean');
pca_shape = h5read(filename, '/shape/model/pcaBasis');
pca_var_shape = h5read(filename, '/shape/model/pcaVariance');

%% load shape representer (polygon mesh)
tri = h5read(filename, '/shape/representer/cells');

%% load landmarks
landmarks = h5read(filename, '/metadata/landmarks/text');

%% prepare and plot data
% note that index in MATLAB starts from 1, not 0
faces1 = double(tri) + 1;
vertices = reshape(mean_shape, 3, size(pca_shape ,2)/3);
clf;
plot_mesh(vertices, faces1);
view(3);

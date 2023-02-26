% This function generates toy examples of all the canonical gaits.

%% Define canonical gait patterns to sample

tripod = repmat([zeros(1,6),ones(1,6)],1,100);
wave = repmat([zeros(1,6),ones(1,30)],1,100);

tetrapod = repmat([zeros(1,6),ones(1,12)],1,100);

% Define the sample length
sample_length = 100;


%% Generate and plot a canonical tetrapod gait

makeFigure;

% Define a step order (limbList);
limbList = {'R3','R2','R1','L3','L2','L1'};

% Plot a step plot using this logical
step = true(6,sample_length);

% Populate the row with the current data
step(1,:) = tetrapod(13:sample_length+12);
step(2,:) = tetrapod(7:sample_length+6);
step(3,:) = tetrapod(1:sample_length);
step(4,:) = tetrapod(1:sample_length);
step(5,:) = tetrapod(13:sample_length+12);
step(6,:) = tetrapod(7:sample_length+6);

% Set the tick marks on the y-axis
set(gca, 'ytick', [1:6]);
set(gca, 'yticklabels', limbList);

% Invert the y-axis
set(gca,'Ydir','reverse');

% Hide the x-axis
set(gca, 'xtick', []);

% Visualize the image
hold on;
imagesc(step);
colormap('gray');

% Provide an x-axis label
xlabel('Time (Steps)');

% Configure the axes
axis('tight');
ConfAxis;
set(gca,'linewidth',6);

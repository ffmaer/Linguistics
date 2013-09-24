clc
%We will construct a graph of nodes and connections between semantic
%concepts, words (lemmas) and their phonemes. First I will label each index
%for the matrix of the graph with the concept it represents.

%Note: Sem1,Sem2,Sem3, and Sem4 are the Semantic features unlabeled in
%figure 1 of Dell Gordon, also letters are doubled in order to not conflict
%with MATLAB constants

Sem1 = 1;
Sem2 = 2;
Sem3 = 3;
Sem4 = 4;
mat = 5;
cat = 6;
hat = 7;
dog = 8;
log = 9;
fog = 10;
mm = 11;
aa = 12;
tt = 13;
kk = 14;
hh = 15;
dd = 16;
oo = 17;
gg = 18;
ll = 19;
ff = 20;
% this process is building the index of the nodes in a graph


%Note: 8 times steps from endnote 5 of Dell Gordon

q_constant = .5;% the rate with which activation decays

weight_constant = .1;% the connection weight between unit i and unit j
strong_weight_constant = .2;
%strong_weight_constant is used to simulate the part of the model that the 
%semantic features of the word "cat" is underscored


network_matrix = zeros(20, 20);
% zeros(20,20) is a function which constructs a 20-by-20 matrices
% with all zeros


for i=1:20,
    network_matrix(i,i) = 1-q_constant;
end
% In a graph, nodes are not connected with themselves.
% But we can put decay rates in nodes, because the behavior of 
% a square matrix multiplying itself well fits the lexical activation model
% in linguisitics.

% Every entry, say (n,n), on the diagonal will influence next matrix's n's
% column and itself. For example:
% 1 0 0          x 0  0
% 1 x 0 ^ 2 ---> x x' 0
% 1 0 0          x 0  0 
% Think the strenth of activation as water.
% And think the nodes, the entries on the diagonal, as tunnel with holes on
% it. Everytime when water passes the tunnel, some water will loose.
% In Linguistics, this phenomenon can be explained as that as time passes,
% the activation on a single node becomes weaker and weaker for two
% reasons. One is the rate which activation decays and the other is
% connection weight.


% this network_matrix is based on the two-step interactive-activation model
network_matrix( Sem1, cat) = strong_weight_constant;
% When Sem1 activates cat we say network_matrix( Sem1, cat)

% In linguistics, this describes a process happening in your brain that
% you have some ideas or meanings that you want to express.

% The first thing come up to your mind is not the exact word,
% not on the lexical level.

% The first thing comes to your mind should be the meaning you want to 
% express, so it is on the semantic level. 

network_matrix( Sem2, cat) = strong_weight_constant;
network_matrix( Sem2, dog) = strong_weight_constant;
network_matrix( Sem3, cat) = strong_weight_constant;
network_matrix( Sem3, dog) = strong_weight_constant;
network_matrix( Sem4, dog) = weight_constant;
network_matrix( mat, mm) = weight_constant;
network_matrix( mat, aa) = weight_constant;
network_matrix( mat, tt) = weight_constant;
network_matrix( cat, Sem1) = strong_weight_constant;
% When cat activates Sem1 we say network_matrix (cat, Sem1)
network_matrix( cat, Sem2) = strong_weight_constant;
network_matrix( cat, Sem3) = strong_weight_constant;
network_matrix( cat, aa) = weight_constant;
network_matrix( cat, tt) = weight_constant;
network_matrix( cat, kk) = weight_constant;
network_matrix( hat, aa) = weight_constant;
network_matrix( hat, tt) = weight_constant;
network_matrix( hat, hh) = weight_constant;
network_matrix( dog, Sem2) = weight_constant;
network_matrix( dog, Sem3) = weight_constant;
network_matrix( dog, Sem4) = weight_constant;
network_matrix( dog, dd) = weight_constant;
network_matrix( dog, oo) = weight_constant;
network_matrix( dog, gg) = weight_constant;
network_matrix( log, oo) = weight_constant;
network_matrix( log, gg) = weight_constant;
network_matrix( log, ll) = weight_constant;
network_matrix( fog, oo) = weight_constant;
network_matrix( fog, gg) = weight_constant;
network_matrix( fog, ff) = weight_constant;
network_matrix( mm, mat) = weight_constant;
network_matrix( aa, mat) = weight_constant;
network_matrix( aa, cat) = weight_constant;
network_matrix( aa, hat) = weight_constant;
network_matrix( tt, mat) = weight_constant;
network_matrix( tt, cat) = weight_constant;
network_matrix( tt, hat) = weight_constant;
network_matrix( kk, cat) = weight_constant;
network_matrix( hh, hat) = weight_constant;
network_matrix( dd, dog) = weight_constant;
network_matrix( oo, dog) = weight_constant;
network_matrix( oo, log) = weight_constant;
network_matrix( oo, fog) = weight_constant;
network_matrix( gg, dog) = weight_constant;
network_matrix( gg, log) = weight_constant;
network_matrix( gg, fog) = weight_constant;
network_matrix( ll, log) = weight_constant;
network_matrix(ff, fog) = weight_constant;

for i=1:8,
    filename = ['matrix/matrix' int2str(i) '.txt'];
    dlmwrite(filename , network_matrix^i, 'newline','pc' ,'delimiter', '\t', 'precision', '%10.5f');
end
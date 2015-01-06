subplot(1,1,1,projection="3d");
u = linspace(0, 2 * pi, 100);
v = linspace(0, pi, 100);

x = outer(cos(u), sin(v));
y = outer(sin(u), sin(v));
z = outer(ones(size(u)), cos(v));
plot_surface(x, y, z,  rstride=4, cstride=4, color='b');

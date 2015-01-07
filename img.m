x = imread("test.png");
w = len(x[0]);
h = len(x);
y = zeros((h,w,4));
z = zeros((h,w,4));
u = zeros((h,w,4));
for d = range(4)
	for i = range(1,h-1)
		for j = range(1,w-1)
			y[i][j][d] = (x[i+1][j][d]+x[i-1][j][d]+x[i][j+1][d]+x[i][j-1][d])/4;
		end
	end
end
for d = range(4)
	for i = range(1,h-1)
		for j = range(1,w-1)
			z[i][j][d] = (y[i+1][j][d]+x[i-1][j][d]+x[i][j+1][d]+x[i][j-1][d])/4;
		end
	end
end
for d = range(4)
	for i = range(1,h-1)
		for j = range(1,w-1)
			u[i][j][d] = (z[i+1][j][d]+x[i-1][j][d]+x[i][j+1][d]+x[i][j-1][d])/4;
		end
	end
end
subplot(221);
imshow(x);
subplot(222);
imshow(y);
subplot(223);
imshow(z);
subplot(224);
imshow(u);

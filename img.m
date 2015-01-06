x = imread("test.png");
w = len(x[0]);
h = len(x);
y = zeros((h,w,4));
for d = range(4)
	for i = range(1,h-1)
		for j = range(1,w-1)
			y[i][j][d] = (x[i+1][j][d]+x[i-1][j][d]+x[i][j+1][d]+x[i][j-1][d])/4;
		end
	end
end
imshow(y)

#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>
#include <ctime>
using namespace cv;
using namespace std;

void printTopText(cv::Mat targetImage, cv::String &text, cv::Scalar color = cv::Scalar(255, 255, 255, 0)) {
	cv::rectangle(targetImage, cv::Rect(8, 0, targetImage.cols - 8, 25), cv::Scalar(0, 0, 0, 0), -1);
	cv::putText(targetImage, text, cv::Point(8, 18), 0, 0.5, color);
}

int main(int argc, char** argv)
{
	std::clock_t timer;
	cv::RNG rng(0xFFFFFFFF);
	const char coolLookingDelay = true;
	const int delayTime = 1; //higher = longer delay per line, lower = shorter delay per line
	const int delayFrequency = 2; //higher = less lines trigger a delay, lower = more lines trigger a delay

	if (argc != 2)
	{
		cout << "Missing input image argument" << endl;
		return -1;
	}

	Mat inputImage, outputImage, displayImage;
	inputImage = imread(argv[1], IMREAD_COLOR); // Read the file
	if (inputImage.empty()) // Check for invalid input
	{
		cout << "Could not open or find the input image" << std::endl;
		return -1;
	}
	outputImage = Mat::zeros(inputImage.size(), inputImage.type());
	displayImage = Mat::zeros(inputImage.rows + 40, (2 * inputImage.cols) + 10 + 20, inputImage.type());
	Rect roiImageAreaOne(Rect(10, 30, inputImage.cols, inputImage.rows));
	Rect roiImageAreaTwo(Rect(inputImage.cols + 20, 30, inputImage.cols, inputImage.rows));
	inputImage.copyTo(displayImage(roiImageAreaOne));

	namedWindow("Hello OpenCV", WINDOW_AUTOSIZE); // Create a window for display
	
	int x, y, c, i; //BGRA (0=BLUE, 1=GREEN, 2=RED, 3=ALPHA/TRANSPARENCY) color scheme

	printTopText(displayImage, cv::String("Press any key to start analysis."));
	imshow("Hello OpenCV", displayImage);
	waitKey(0);

	//Show green
	printTopText(displayImage, cv::String("Extracting green color layer..."));
	for (y = 0; y < inputImage.rows; y++) {
		for (x = 0; x < inputImage.cols; x++) {
			for (c = 0; c < 3; c++) {
				outputImage.at<Vec3b>(y, x)[c] =
					(inputImage.at<Vec3b>(y, x)[1]);
			}
		}
		if (y % delayFrequency == 0) {
			inputImage.copyTo(displayImage(roiImageAreaOne));
			if (y < inputImage.rows - 5)
				cv::line(displayImage, cv::Point(10, 30 + y),
						 cv::Point(inputImage.cols + 9, 30 + y), cv::Scalar(255, 255, 255, 0));	
			outputImage.copyTo(displayImage(roiImageAreaTwo));
			imshow("Hello OpenCV", displayImage);
			if (coolLookingDelay) waitKey(delayTime);
		}
	}

	//Show red
	printTopText(displayImage, cv::String("Extracting red color layer..."));
	for (y = 0; y < inputImage.rows; y++) {
		for (x = 0; x < inputImage.cols; x++) {
			for (c = 0; c < 3; c++) {
				outputImage.at<Vec3b>(y, x)[c] =
					(inputImage.at<Vec3b>(y, x)[2]);
			}
		}
		if (y % delayFrequency == 0) {
			inputImage.copyTo(displayImage(roiImageAreaOne));
			if(y < inputImage.rows - 5)
				cv::line(displayImage, cv::Point(10, 30 + y),
					cv::Point(inputImage.cols + 9, 30 + y), cv::Scalar(255, 255, 255, 0));
			outputImage.copyTo(displayImage(roiImageAreaTwo));
			imshow("Hello OpenCV", displayImage);
			if (coolLookingDelay) waitKey(delayTime);
		}
	}

	//Show subtracted
	printTopText(displayImage, cv::String("Subtracting..."));
	for (y = 0; y < inputImage.rows; y++) {
		for (x = 0; x < inputImage.cols; x++) {
			for (c = 0; c < 3; c++) {
				outputImage.at<Vec3b>(y, x)[c] =
					saturate_cast<uchar>((inputImage.at<Vec3b>(y, x)[1]) - (inputImage.at<Vec3b>(y, x)[2]));
			}
		}
		if (y % delayFrequency == 0) {
			outputImage.copyTo(displayImage(roiImageAreaTwo));
			imshow("Hello OpenCV", displayImage);
			if (coolLookingDelay) waitKey(delayTime);
		}
	}

	//apply blur
	printTopText(displayImage, cv::String("Applying median blur..."));
	cv::Mat blurOutputBufferImage = cv::Mat(outputImage.rows, outputImage.cols, outputImage.type());
	cv::medianBlur(outputImage, blurOutputBufferImage, 5);
	for (y = 0; y < inputImage.rows; y++) {
		for (x = 0; x < inputImage.cols; x++) {
			outputImage.at<Vec3b>(y, x) = blurOutputBufferImage.at<Vec3b>(y, x);
		}
		if (y % delayFrequency == 0) {
			outputImage.copyTo(displayImage(roiImageAreaTwo));
			if (y < inputImage.rows - 5)
				cv::line(displayImage, cv::Point(roiImageAreaTwo.x, 30 + y),
						 cv::Point(roiImageAreaTwo.x + roiImageAreaTwo.width - 1, 30 + y), cv::Scalar(255, 255, 255, 0));
			imshow("Hello OpenCV", displayImage);
			if (coolLookingDelay) waitKey(delayTime);
		}
	}

	printTopText(displayImage, cv::String("Image processing complete. Press any key to exit."));
	inputImage.copyTo(displayImage(roiImageAreaOne));
	outputImage.copyTo(displayImage(roiImageAreaTwo));
	imshow("Hello OpenCV", displayImage);

	while (1) {
		printTopText(displayImage, cv::String("Image processing complete. Press any key to exit."));
		imshow("Hello OpenCV", displayImage);
		if (waitKey(400) != -1) break;
		printTopText(displayImage, cv::String(""));
		imshow("Hello OpenCV", displayImage);
		if (waitKey(400) != -1) break;
	}

	return 0;
}
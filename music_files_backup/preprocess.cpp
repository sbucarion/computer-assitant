#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>

int main(){

    /*create input array: matrix*/
    /*also populate matrix with zeros*/
    cv::Mat input = cv::Mat::zeros( cv::Size(400, 400), CV_8UC3);

    /*draw a circle on input*/
    cv::circle(input, cv::Point(200, 200), 100.0, cv::Scalar (0, 0, 255), 1, 8);

    /*display input*/
    imshow("input", input);

    /*stores the output*/
    cv::Mat output;

    /*compute the bitwise not of input array*/
    /*and store them in output array*/
    bitwise_not(input, output);

    /*display the output*/
    imshow("bitwise_not", output);

    /*wait for the use to press any */
    /*key to exit frames*/
    cv::waitKey(0);

    /*return 0 to caller to indicate*/
    /*successful termination of program*/
    return 0;
}
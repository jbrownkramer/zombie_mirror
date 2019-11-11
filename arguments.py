import argparse

def parsed_args():
    # construct the argument parser and parse the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-c","--cameraorientation",default=180,type=int,choices=[0,90,180,270], help="How you've oriented the camera")
    parser.add_argument("-d","--displayorientation",default=270,type=int,choices=[0,90,180,270], help="How you've oriented the display")
    parser.add_argument("-m", "--mirrored", type=bool, default=False, help="Configure true if the image is mirrored")
    parser.add_argument("--minfacesize", type=int, default=128, help="Min detected face size in the original image")
    parser.add_argument("--zombietime", type=float, default=5, help="Time is seconds to display zombie image")
    parser.add_argument("-f","--fontsize", type=int, default=128, help="Size of font")
    parser.add_argument("-r","--cameraresolution", type=resolution, default=(1920,1080), help="Desired Camera Resolution")
    parser.add_argument("-t","--webtimeout", type=float, default=6, help="Time it will wait for response from server")


    return parser.parse_args()

def resolution(s):
    try:
        tokens = s.strip().split("x")
        return int(tokens[0]),int(tokens[1])
    except:
        raise argparse.ArgumentTypeError("Resolution must be of the form WxH")
from interface import FeatureExtractor
from feature.image import ImageFeatureExtractor
from fast_rcnn.config import cfg, get_output_dir

def test():
    prototxt = '/mnt/fileserver/shared/vital/image-features/test.prototxt'
    weights = '/mnt/fileserver/shared/vital/image-features/resnet101_faster_rcnn_final_iter_320000_for_36_bboxes.caffemodel'
    imagesPath = 'images'
    imagePrefix = ''
    cfg.TEST.HAS_RPN = 'TRUE'
    extractor = ImageFeatureExtractor(prototxt, weights, imagesPath, imagePrefix)

    image_id = 'Fat-Zebra-Animated-Animal-Photo' 
    extractor.getFeaturesByImageId(image_id)

test()

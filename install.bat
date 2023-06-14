git clone https://github.com/SugaR256/imedit2.git
cd imedit2
curl.exe -o retinanet.pth https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/retinanet_resnet50_fpn_coco-eeacb38b.pth
pip install -r requirements.txt
python main.py
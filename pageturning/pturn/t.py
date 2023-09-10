import cv2, numpy as np
import matplotlib.pylab as plt
from time import sleep

img1 = cv2.imread("C:/Users/WHO A U/Desktop/p1f.png")
img2 = cv2.imread("C:/Users/WHO A U/Desktop/p2f.png")
img3 = cv2.imread("C:/Users/WHO A U/Desktop/p3f.png")
img4 = cv2.imread("C:/Users/WHO A U/Desktop/p4f.png")


imgs = [img1, img2, img3, img4]
original_imgs = [img1, img2, img3, img4]

hists = []
original_hists = []

for i, img in enumerate(imgs) :
    plt.subplot(1,len(imgs),i+1)
    plt.title('img%d'% (i+1))
    plt.axis('off') 
    plt.imshow(img[:,:,::-1])
    #---① 각 이미지를 HSV로 변환
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    #---② H,S 채널에 대한 히스토그램 계산
    hist = cv2.calcHist([hsv], [0,1], None, [180,256], [0,180,0, 256])
    #---③ 0~1로 정규화
    cv2.normalize(hist, hist, 0, 1, cv2.NORM_MINMAX)
    hists.append(hist)

for k, original_img in enumerate(original_imgs) :
    plt.subplot(1,len(original_imgs),k+1)
    plt.title('img%d'% (k+1))
    plt.axis('off') 
    plt.imshow(original_img[:,:,::-1])
    #---① 각 이미지를 HSV로 변환
    original_hsv = cv2.cvtColor(original_img, cv2.COLOR_BGR2HSV)
    #---② H,S 채널에 대한 히스토그램 계산
    original_hist = cv2.calcHist([original_hsv], [0,1], None, [180,256], [0,180,0, 256])
    #---③ 0~1로 정규화
    cv2.normalize(original_hist, original_hist, 0, 1, cv2.NORM_MINMAX)
    original_hists.append(original_hist)


query1 = original_hists[0]
query2 = original_hists[1]
query3 = original_hists[2]
query4 = original_hists[3]

methods = {'CORREL' :cv2.HISTCMP_CORREL, 'CHISQR':cv2.HISTCMP_CHISQR, 
           'INTERSECT':cv2.HISTCMP_INTERSECT,
           'BHATTACHARYYA':cv2.HISTCMP_BHATTACHARYYA}

for j, (name, flag) in enumerate(methods.items()):
    print('%-10s\t'%name)
    for i, (hist, img) in enumerate(zip(hists, imgs)):
        #---④ 각 메서드에 따라 img1과 각 이미지의 히스토그램 비교
        ret1 = cv2.compareHist(query1, hist, flag)
        if flag == cv2.HISTCMP_INTERSECT: #교차 분석인 경우 
            ret1 = ret1/np.sum(query1)      #비교대상으로 나누어 1로 정규화
        print("img%d:%7.2f\t"% (i+1 , ret1))

        if ret1 == 0:
            print("마디1")
            cv2.imshow('query1', img1)
            

for j, (name, flag) in enumerate(methods.items()):
    print('%-10s\t'%name)
    for i, (hist, img) in enumerate(zip(hists, imgs)):
        #---④ 각 메서드에 따라 img1과 각 이미지의 히스토그램 비교
        ret2 = cv2.compareHist(query2, hist, flag)
        if flag == cv2.HISTCMP_INTERSECT: #교차 분석인 경우 
            ret2 = ret2/np.sum(query2)      #비교대상으로 나누어 1로 정규화
        print("img%d:%7.2f\t"% (i+1 , ret2))

        if ret2 == 0:
            print("마디2")
            cv2.imshow('query2', img2)
            
for j, (name, flag) in enumerate(methods.items()):
    print('%-10s\t'%name)
    for i, (hist, img) in enumerate(zip(hists, imgs)):
        #---④ 각 메서드에 따라 img1과 각 이미지의 히스토그램 비교
        ret3 = cv2.compareHist(query3, hist, flag)
        if flag == cv2.HISTCMP_INTERSECT: #교차 분석인 경우 
            ret3 = ret3/np.sum(query3)      #비교대상으로 나누어 1로 정규화
        print("img%d:%7.2f\t"% (i+1 , ret3))

        if ret3 == 0:
            print("마디3")
            cv2.imshow('query3', img3)
            
for j, (name, flag) in enumerate(methods.items()):
    print('%-10s\t'%name)
    for i, (hist, img) in enumerate(zip(hists, imgs)):
        #---④ 각 메서드에 따라 img1과 각 이미지의 히스토그램 비교
        ret4 = cv2.compareHist(query4, hist, flag)
        if flag == cv2.HISTCMP_INTERSECT: #교차 분석인 경우 
            ret4 = ret4/np.sum(query4)      #비교대상으로 나누어 1로 정규화
        print("img%d:%7.2f\t"% (i+1 , ret4))

        if ret4 == 0:
            print("마디4")
            cv2.imshow('query4', img4)            
          
    print()
plt.show()
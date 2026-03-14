import cv2 as cv2

#carregar uma image
imagem = cv2.imread("OpenCV/pngwing.com.png,cv2.IMREAD_COLOR")

# resize
escala = 0.5
altura = int(imagem.shape[0] * escala)
largura = int(imagem.shape[1] * escala)
dimensoes = (largura, altura)

imagem = cv2.resize(imagem, dimensoes, interpolation=cv2.INTER_AREA)

#exibir a imagem
cv2.imshow("Imagem", imagem)

#esperar até que uma tecla seja pressionada
cv2.waitKey(0)
cv2.destroyAllWindows()
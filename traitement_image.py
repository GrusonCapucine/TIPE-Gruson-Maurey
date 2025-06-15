import cv2
import numpy as np

def detect_stars(image_path, output_path="output_with_stars.png"):
    # Charger l'image en niveaux de gris
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Appliquer un seuillage pour isoler les étoiles brillantes
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    # Trouver les contours des zones blanches (les étoiles)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    star_coords = []

    for contour in contours:
        # Calculer le centre du contour
        M = cv2.moments(contour)
        if M["m00"] == 0:
            continue  # éviter la division par zéro

        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        star_coords.append((cx, cy))

        """
        # Dessiner un cercle rouge autour de l'étoile détectée
        (x, y), radius = cv2.minEnclosingCircle(contour)
        center = (int(x), int(y))
        radius = int(radius)
        cv2.circle(image, center, radius+2, (0, 0, 255), 1)

    # Sauvegarder l'image annotée
    cv2.imwrite(output_path, image)
    """
    return star_coords

"""
# Exemple d'utilisation
image_file = "./Test_stel/photo.png"
coords = detect_stars(image_file)
print("Coordonnées des étoiles détectées :", coords)
"""

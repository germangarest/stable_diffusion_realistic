# RealGEN

Esta aplicación web permite generar imágenes **realistas** utilizando la API de Stable Diffusion Web UI. En lugar de que el usuario deba escribir un prompt manualmente, se ofrecen diversos controles interactivos (selectboxes, sliders, checkboxes, etc.) para configurar los parámetros deseados. La aplicación traduce estas selecciones en un prompt detallado que se envía a la API para generar la imagen.

<img src="img/logo.png" alt="realismo" width="400"/>

Este proyecto se realizó como parte del curso de *Máster de FP en Inteligencia Artificial y Big Data*.

## Integrantes del equipo

| [![Jairo Andrades Bueno](https://github.com/jairopo.png?size=100)](https://github.com/jairopo) | [![Germán García Estévez](https://github.com/germangarest.png?size=100)](https://github.com/germangarest) |
|:----------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------:|
| **Jairo Andrades Bueno**                                                                       | **Germán García Estévez**                                                                       |

## Modelo Utilizado

- **Nombre:** Re3mix-realisticV2-Hyper
- **Descripción:**  
  Este modelo completo en formato safetensors está diseñado para generar imágenes de alta fidelidad y realismo, capturando detalles precisos y una estética visual similar a la fotografía. Es ideal para crear retratos, paisajes, escenas urbanas o naturales con un nivel de detalle excepcional.
- **Enlace:** [Re3mix-realisticV2-Hyper en Civitai](https://civitai.com/models/560176/re3mix-realisticv2-hyper?modelVersionId=623806)

## Características de la Aplicación

- **Interfaz Web Interactiva:**  
  Desarrollada en *Streamlit*, que permite una experiencia sencilla e intuitiva.
- **Selección de Parámetros:**  
  El usuario puede elegir entre diferentes opciones para definir:
  - **Tipo de escena:** Por ejemplo, Retrato, Paisaje, Urbano, Natural, Nocturno.
  - **Estado de ánimo:** Ejemplos: sereno, vibrante, melancólico, dinámico, misterioso.
  - **Fondo o ambientación:** Ejemplos: ciudad, naturaleza, interior, atardecer, amanecer.
  - **Nivel de detalle y saturación:** Configurables mediante sliders (porcentaje de detalle y vivacidad de colores).
  - **Elementos adicionales:** Opciones como efectos de luz, composición artística, iluminación dramática, alta resolución, detalles intrincados.
- **Generación Automática del Prompt:**  
  Las opciones seleccionadas se combinan para formar un prompt detallado en inglés que se envía a la API de Stable Diffusion Web UI.
- **Integración con la API de Stable Diffusion:**  
  Permite generar imágenes de forma remota, aprovechando el poder del modelo seleccionado.

## Uso

- **Configuración de Parámetros:**  
  Utiliza la barra lateral para seleccionar el tipo de escena, estado de ánimo, fondo, nivel de detalle, saturación y otros elementos adicionales.
- **Visualización del Prompt:**  
  La aplicación muestra el prompt generado a partir de tus selecciones para que puedas revisarlo.
- **Generación de la Imagen:**  
  Haz clic en el botón **"Generar Imagen"** para enviar el prompt a la API y obtener la imagen generada, la cual se mostrará en la interfaz.

## Capturas de Pantalla y Ejemplos

_A continuación, se muestran algunas capturas de pantalla de la aplicación en funcionamiento y ejemplos de imágenes generadas:_

<img src="img/interfaz.png" alt="interfaz" width="400"/>
<img src="img/imagen_1.png" alt="imagen" width="400"/>

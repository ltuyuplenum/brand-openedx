# Interfaz del Paquete de Marca de Open edX

Este proyecto contiene los recursos de marca (branding) y el estilo predeterminado utilizados en las aplicaciones de Open edX. Está publicado en npm como `@openedx/brand-openedx`.

La estructura de archivos sirve como una interfaz que debe implementarse para la personalización de la marca y el tema visual de Open edX.

## Cómo usar este paquete

Las aplicaciones en Open edX están configuradas de forma predeterminada para incluir este paquete para los recursos de marca y el estilo visual del tema.

Para utilizar una marca y un tema personalizados...

1.  Haz un fork o copia este proyecto. Asegúrate de que resida en una ubicación accesible para las aplicaciones de Open edX durante la compilación de recursos (builds). Puede ser un repositorio de git publicado, un paquete de npm o una carpeta local, según tu caso.
2.  Reemplaza los recursos en este proyecto con tus propios logotipos y tokens de diseño. Haz coincidir los nombres de archivo exactamente. Las aplicaciones de Open edX hacen referencia a estos archivos mediante su ruta de archivo. Consulta la marca de edx.org en <https://github.com/edx/brand> como ejemplo.

    La personalización del tema se realiza a través de tokens de diseño; sigue la guía en [Compatibilidad con Tokens de Diseño de Paragon](./docs/how-to/design-tokens-support.rst).

3.  Configura tu instancia de Open edX para consumir tu paquete de marca personalizado. Consulta esta documentación sobre cómo configurar la plataforma:
    https://docs.openedx.org/projects/openedx-proposals/en/latest/architectural-decisions/oep-0048-brand-customization.html
    [TODO: Agregar un enlace a la documentación sobre la configuración en los pipelines de MFE de Open edX cuando esté disponible]
4.  Vuelve a compilar los recursos y microfrontends en tu instancia de Open edX para ver reflejada la nueva marca. [TODO: Agregar enlace a la documentación pertinente cuando esté completa].

## Archivos que este paquete debe poner a disposición

`/logo.svg`

![logo](/logo.svg)

`/logo-trademark.svg` Una variante del logotipo con marca registrada ® o ™.
Nota: Este archivo debe estar presente. Si no tienes una variante con marca registrada de tu logotipo, copia tu logotipo regular y utiliza ese.

![logo](/logo-trademark.svg)

`/logo-white.svg` Una variante del logotipo para usar en fondos oscuros.

![logo](/logo-white.svg)

`/favicon.ico` El favicon del sitio.

![favicon](/favicon.ico)

`/paragon/images/card-imagecap-fallback.png` Una variante de la imagen de reserva (fallback) predeterminada para el componente [Card.ImageCap].

![card-imagecap-fallback](/paragon/images/card-imagecap-fallback.png)

`/core.min.css` (y `/core.css`) Paquete CSS principal de la capa de marca, ensamblado a partir de `paragon/core.scss` mediante `paragon build-scss` al momento de la publicación. Las aplicaciones que lo consumen importan esto sobre el CSS principal propio de Paragon.

`/light.min.css` (y `/light.css`) Paquete CSS de la variante de tema claro (light theme), ensamblado a partir de las salidas de tokens en `paragon/build/themes/light/`. Las aplicaciones que lo consumen importan esto para el tema claro.

## Archivos fuente (para forks que personalicen la marca)

Estos archivos residen en este repositorio como entradas para la compilación (build); no se envían en el paquete publicado.

`/paragon/core.scss` Punto de ensamblaje consumido por `paragon build-scss` y generado como el archivo publicado `core.min.css`. Su función es hacer `@use` del CSS generado por tokens en `./build/core/...` para que esas propiedades personalizadas (custom properties) terminen en el paquete que descargan los consumidores. Con Paragon 23, aquí no es donde van las personalizaciones de marca (utiliza tokens de diseño para ello), sino que es el lugar para añadidos que no se pueden tokenizar, como reglas `@media` personalizadas o selectores específicos de la marca que no correspondan a componentes de Paragon.

`/paragon/_fonts.scss` Parcial de SASS para reglas `@import` que cargan fuentes web referenciadas por los tokens (por ejemplo, URLs de Google Fonts).

`/paragon/tokens/core/<category>/*.json`,
`/paragon/tokens/themes/<variant>/*.json` Sobrescrituras de tokens de diseño en formato [Style Dictionary](https://styledictionary.com/), y la única forma admitida de personalizar el tema con Paragon 23. Los archivos bajo `core/` sobrescriben los tokens principales de Paragon (tipografía, espaciado, breakpoints, etc.); los archivos bajo `themes/<variant>/` sobrescriben los tokens de la variante de tema (colores, valores de componentes) para dicha variante (actualmente `light`). Consulta [Compatibilidad con Tokens de Diseño de Paragon](./docs/how-to/design-tokens-support.rst).

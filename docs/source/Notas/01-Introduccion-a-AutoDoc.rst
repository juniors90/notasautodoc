Introducción a AutoDoc
==================================

AutoDoc_ es un paquete **GAP** que está destinado a ayudar a los autore
de paquetes **GAP** a crear y mantener la documentación de sus paquetes.
En esta capacidad, se basa en GAPDoc_ y no reemplaza a GAPDoc_, sino que
lo complementa.

En este capítulo describimos cómo empezar a utilizar AutoDoc_ para su
paquete. Primero, explicamos en la Sección :ref:`creando-manual-desde-cero`
cómo escribir un nuevo manual de paquete desde cero.

Luego mostramos en la Sección 1.3 cómo podemos beneficiarnos de AutoDoc_
incluso si ya tiene un manual completo escrito usando GAPDoc_.

En la Sección 1.4, explicamos cómo puede usar AutoDoc_ para generar una
página de título y el archivo XML principal para su manual.

Finalmente, la Sección 1.5 explica qué son las hojas de trabajo de AutoDoc_
y cómo usarlas.

.. _creando-manual-desde-cero:

Creando un manual del paquete desde cero
-------------------------------------------

Suponga que su paquete ya está en funcionamiento, pero hasta ahora no
tiene manual. Luego, puede generar rápidamente un "``scaffold``" para el
manual de un paquete usando el comando AutoDoc (4.1.1) como este,
mientras ejecuta **GAP** desde el directorio de su paquete (el que
contiene el archivo ``PackageInfo.g``):

.. code-block:: gap
    :caption: Generando un "scaffold"
    :name: generando_un_scaffold
    :linenos:

    LoadPackage( "AutoDoc" );
    AutoDoc( rec( scaffold := true ) );


Esto primero lee el archivo ``PackageInfo.g`` del directorio actual.
Extrae información sobre el paquete de él (como su nombre y versión,
consulte la Sección 1.4.1). Luego crea dos archivos XML
``doc/NOMBRE_DE_TU_PAQUETE.xml`` y ``doc/title.xml`` dentro del
directorio del paquete. Finalmente, ejecuta GAPDoc_ en ellos para
producir una buena versión inicial en **PDF** y **HTML** de su
nuevo manual.

Para asegurarnos de que el sistema de ayuda de **GAP** recoja el
manual de su paquete, también debemos agregar lo siguiente al
fichero ``PackageInfo.g``:

.. code-block:: gap
    :caption: Para recoger el manual
    :name: para_recoger_el_manual
    :linenos:

    PackageDoc := rec(
        BookName := ~.PackageName,
        ArchiveURLSubset := ["doc"],
        HTMLStart := "doc/chap0.html",
        PDFFile := "doc/manual.pdf",
        SixFile := "doc/manual.six",
        LongTitle := ~.Subtitle,
    ),

Ahora sí, nuestro paquete tiene un manual de trabajo mínimo.
Por supuesto, estará casi vacío por ahora, pero ya debería contener
información útil, basada en los datos de su ``PackageInfo.g``.
Esto incluye el nombre, la versión y la descripción de su paquete,
así como información sobre sus autores. Y si alguna vez cambia los
datos del paquete (por ejemplo, porque cambió su dirección de correo
electrónico), simplemente vuelva a ejecutar el comando anterior para
volver a generar los dos archivos XML principales con la información
más reciente.

A continuación, por supuesto, debemos proporcionar contenido real
(desafortunadamente, aún no pudimos automatizarlo para usted, se
requiere más investigación sobre inteligencia artificial).
Para agregar más contenido, tiene varias opciones:
Puede agregar más archivos XML GAPDoc_ que contengan capítulos,
secciones adicionales, etc.
O puede utilizar los comentarios fuente clásicos de GAPDoc_
(en cualquier caso, consulte la Sección 1.3 sobre cómo enseñar al
comando AutoDoc (4.1.1) para incluir esta documentación adicional).
O puede utilizar las facilidades de documentación especiales que
proporciona AutoDoc_ (consulte la Sección :ref:`documentar-codigo-con-autodoc`).

Probablemente desee volver a ejecutar el comando AutoDoc (4.1.1)
con frecuencia, por ejemplo. cada vez que modificó su documentación
o su ``PackageInfo.g``. Para que esto sea más conveniente y reproducible,
recomendamos colocar su invocación en un archivo ``makedoc.g``
en el directorio de su paquete, con contenido basado en el siguiente ejemplo:

.. code-block:: gap
    :caption: makedoc.g
    :name: makedoc.g
    :linenos:
    
    LoadPackage( "AutoDoc" );
    AutoDoc( rec( autodoc := true ) );
    QUIT;

Luego, puede volver a generar el manual del paquete desde la línea de
comando con el siguiente comando, ejecutado desde dentro del directorio
del paquete:

.. code-block:: gap
    :caption: makedoc.g desde la línea de comandos
    :name: gap_makedoc.g
    :linenos:
    
    gap makedoc.g

.. _documentar-codigo-con-autodoc:

Documentar código con AutoDoc
----------------------------------------

Para que una de sus funciones, operaciones, atributos, etc.,
globales aparezcan en el manual del paquete, simplemente inserte
un comentario AutoDoc_ de la forma ``#!`` directamente en frente de él.
Por ejemplo:

.. code-block:: gap
    :caption: Comentarios del tipo AutoDoc
    :name: comentarios_iniciales
    :linenos:
    
    #!
    DeclareOperation( "ToricVariety", [ IsConvexObject ] );

Este pequeño cambio ya es suficiente para que la operación aparezca en
el manual. En general, querrá agregar más información sobre la operación,
como en el siguiente ejemplo:

.. code-block:: gap
    :caption: Comentarios descriptivos en AutoDoc
    :name: comentarios_descriptivos
    :linenos:
    
    #! @Arguments conv
    #! @Returns una variedad tórica
    #! @Description
    #! Crea una variedad tórica
    #! del objeto convexo <A>conv</A>.
    DeclareOperation( "ToricVariety", [ IsConvexObject ] );

Para obtener una descripción detallada de lo que puede hacer
con los comentarios de la documentación de AutoDoc_, consulte
el Capítulo 2.

Suponga que no ha estado usando GAPDoc_ antes, sino que utilizó
el proceso descrito en la Sección :ref:`creando-manual-desde-cero`
para crear su manual. Luego, el siguiente comando **GAP** regenerará
el manual e incluirá automáticamente todas las funciones, operaciones, etc.

.. code-block:: gap
    :caption: incluir automáticamente la documentación de la API
    :name: incluir_automaticamente_la_documentacion 
    :linenos:
    
    LoadPackage( "AutoDoc" );
    AutoDoc( rec( scaffold := true,
                  autodoc := true ) );


Si no está utilizando la función de ``scaffold``, por ejemplo,
debido a que ya tiene un manual basado en GAPDoc_ existente,
aún puede usar los comentarios de la documentación de AutoDoc_.
Solo asegúrese de editar primero el archivo XML principal de su
documentación e inserte la línea

.. code-block:: gap
    :caption: Include SYSTEM
    :name: AutoDocMainFile.xml 
    :linenos:
    
    #Include SYSTEM "_AutoDocMainFile.xml"

en un lugar adecuado. Esto significa que puede mezclar los
comentarios de la documentación de AutoDoc_ libremente con su
documentación existente; incluso puede hacer uso de cualquier
comentario de documentación de GAPDoc_ existente en su código.
El siguiente comando debería serle útil en este caso; todavía
escanea el código del paquete en busca de comentarios de
documentación de AutoDoc_ y ejecuta GAPDoc_ para producir una
salida **HTML** y **PDF**, pero no toca los archivos XML de la
documentación de otra manera.

.. code-block:: gap
    :caption: AutoDoc y GAPDoc
    :name: AutoDoc_GAPDoc 
    :linenos:
    
    LoadPackage( "AutoDoc" );
    AutoDoc( rec( autodoc := true ) );


Uso de AutoDoc en un manual de GAPDoc existente
-----------------------------------------------

Incluso si ya tiene un manual de GAPDoc_ existente, puede
resultarle interesante utilizar AutoDoc para dos propósitos:

En primer lugar, con AutoDoc_ es muy conveniente regenerar tu
documentación.

En segundo lugar, la función de andamiaje que genera una página
de título con todos los metadatos de su paquete de manera uniforme
es muy útil. El proceso algo tedioso de mantener su página de título
sincronizada con su ``PackageInfo.g`` está completamente automatizado
de esta manera (incluida la versión correcta, los datos de publicación,
la información del autor, etc.).

Hay varios ejemplos de paquetes que utilizan AutoDoc_ solo para este
propósito, por ejemplo ``io`` y ``orb``.

Uso de AutoDoc en un manual completo de GAPDoc
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Suponga que ya tiene un manual XML completo, con algunos archivos
``XML`` principales y de título y algo de documentación para las
operaciones distribuidas en todos sus archivos ``.g``, ``.gd`` y ``.gi``.
Suponga que el archivo ``XML`` principal se llama ``PACKAGENAME.xml``
y está en el subdirectorio ``/doc`` de su paquete.
Luego, puede reconstruir su manual ejecutando los siguientes dos
comandos **GAP** desde una sesión **GAP** iniciada en el directorio
raíz de su paquete:

.. code-block:: gap

    LoadPackage( "AutoDoc" );
    AutoDoc( );

En contraste, RingsForHomalg actualmente usa esencialmente el siguiente
código en su archivo ``makedoc.g`` para lograr el mismo resultado

.. code-block:: gap

    LoadPackage( "GAPDoc" );
    SetGapDocLaTeXOptions( "utf8" );
    bib := ParseBibFiles( "doc/RingsForHomalg.bib" );
    WriteBibXMLextFile( "doc/RingsForHomalgBib.xml", bib );
    list := [
        "../gap/RingsForHomalg.gd",
        "../gap/RingsForHomalg.gi",
        "../gap/Singular.gi",
        "../gap/SingularBasic.gi",
        "../examples/RingConstructionsExternalGAP.g",
        "../examples/RingConstructionsSingular.g",
        "../examples/RingConstructionsMAGMA.g",
        "../examples/RingConstructionsMacaulay2.g",
        "../examples/RingConstructionsSage.g",
        "../examples/RingConstructionsMaple.g",
    ];
    MakeGAPDocDoc( "doc", "RingsForHomalg", list, "RingsForHomalg" );
    GAPDocManualLab( "RingsForHomalg" );

Tenga en cuenta que, en particular, no tiene que preocuparse por
mantener actualizada una lista de sus archivos de implementación.

Pero hay más. AutoDoc_ puede crear archivos ``.tst`` a partir de
los ejemplos de su manual para probar su paquete.
Esto se puede lograr a través de

.. code-block::

    LoadPackage( "AutoDoc" );
    AutoDoc( rec( extract_examples := true ) );

Ahora los archivos ``PACKAGENAME01.tst``, ``PACKAGENAME02.tst`` y
así aparecen en el subdirectorio ``tst/`` de su paquete, y se pueden
probar como de costumbre usando ``Test`` (Referencia: Test)
respectivamente ``TestDirectory`` (Referencia: TestDirectory).

Configurar diferentes opciones de GAPDoc
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A veces, los valores predeterminados para el comando GAPDoc_ utilizado
por AutoDoc_ pueden no ser adecuados para su manual.

Suponga que su archivo XML principal no se llama ``PACKAGENAME.xml``,
sino algo más, por ejemplo ``main.xml``. Luego puede decirle a AutoDoc_
que use este archivo como el archivo XML principal a través de

.. code-block::

    LoadPackage( "AutoDoc" );
    AutoDoc( rec( gapdoc := rec( main := "main" ) ) );


Como se explicó anteriormente, AutoDoc_ escanea por defecto todos
los archivos ``.g``, ``.gd`` y ``.gi`` que puede encontrar dentro
del directorio raíz de su paquete, y también en los subdirectorios
``gap``, ``lib``, ``examples`` y ``examples/doc``.

Si mantiene los archivos de origen con documentación en otros
directorios, puede ajustar la lista de directorios que AutoDoc_
analiza mediante la opción ``scan_dirs``. El siguiente ejemplo
ilustra esto indicando a AutoDoc_ que busque solo en el
subdirectorio ``package_sources`` del directorio raíz de los
paquetes.

.. code-block:: gap
    :linenos:

    LoadPackage( "AutoDoc" );
    AutoDoc( rec( gapdoc := rec( scan_dirs := [ "package_sources" ] ) ) );


También puede especificar una lista explícita de archivos que
contienen documentación, que se buscará además de cualquier
archivo ubicado dentro de los directorios de exploración:

.. code-block:: gap
    :linenos:

    LoadPackage( "AutoDoc" );
    AutoDoc( rec( gapdoc := rec( files := [ "path/to/some/hidden/file.gds" ] ) ) );

Dar un archivo de este tipo no evita que los ``scan_dirs`` estándar
se escaneen en busca de otros archivos.

A continuación, GAPDoc_ admite la creación de la documentación con
rutas relativas. Esto significa que los enlaces a manuales de otros
paquetes o la biblioteca **GAP** no serán absolutos, sino relativos
a su documentación. Esto puede ser particularmente útil si desea
crear un tarball de lanzamiento o mover la instalación de **GAP** más
adelante. Suponga que está iniciando **GAP** en la ruta raíz de su
paquete como siempre, y la llamada estándar de ``AutoDoc (4.1.1)`` luego
construirá la documentación en el subdirectorio doc de su paquete.
Desde este directorio, el directorio raíz de gap tiene la ruta relativa
``../../..``. Entonces puede habilitar las rutas relativas por

.. code-block:: gap
    :linenos:
    
    LoadPackage( "AutoDoc" );
    AutoDoc( rec( gapdoc := rec( gap_root_relative_path := "../../.." ) ) );

o, ya que ``../../..`` es la opción estándar para ``gap_root_relative_path``, por

.. code-block:: gap
    :linenos:
    
    LoadPackage( "AutoDoc" );
    AutoDoc( rec( gapdoc := rec( gap_root_relative_path := true ) ) );


Convertir un manual de GAPDoc existente para utilizar AutoDoc
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. _AutoDoc: https://gap-packages.github.io/AutoDoc/

.. _GAPDoc: http://www.math.rwth-aachen.de/~Frank.Luebeck/GAPDoc/index.html
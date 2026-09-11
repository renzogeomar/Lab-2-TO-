error id: file://<WORKSPACE>/Profesor.java:java/util/List#
file://<WORKSPACE>/Profesor.java
empty definition using pc, found symbol in pc: java/util/List#
empty definition using semanticdb
empty definition using fallback
non-local guesses:

offset: 322
uri: file://<WORKSPACE>/Profesor.java
text:
```scala
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

class Profesor extends Persona {
    private String materia;

    public Profesor(String nombre, int edad, Curso curso) {
        super(nombre, edad);
        this.materia = materia;
        this.cursos = new ArrayList<>();
    }

    public >L@@ist<String getCursos() {
        return cursos;
    }

    public void agregarCurso(String curso) {
        cursos.add(curso);
    }

    @Override
    public String toString() {
        return super.toString() + ", Materia: " + materia + ", Cursos: " + cursos;
    }

}
```


#### Short summary: 

empty definition using pc, found symbol in pc: java/util/List#
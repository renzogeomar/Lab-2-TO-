error id: file://<WORKSPACE>/Profesor.java:_empty_/cursos#
file://<WORKSPACE>/Profesor.java
empty definition using pc, found symbol in pc: _empty_/cursos#
empty definition using semanticdb
empty definition using fallback
non-local guesses:

offset: 362
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

    public List<String> getCursos() {
        return @@cursos;
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

empty definition using pc, found symbol in pc: _empty_/cursos#
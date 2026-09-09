import java.util.ArrayList;
import java.util.List;

class Universidad {
    private String nombre;
    private List<Curso> cursos;

    public Universidad(String nombre) {
        this.nombre = nombre;
        this.cursos = new ArrayList<>();
    }

    public void agregarCurso(Curso curso) {
        this.cursos.add(curso);
    }

    public String getNombre() { return nombre; }
    public void setNombre(String nombre) { this.nombre = nombre; }
    public List<Curso> getCursos() { return cursos; }
    public void setCursos(List<Curso> cursos) { this.cursos = cursos; }

    @Override
    public String toString() {
        return "Universidad: " + nombre + " | Total cursos: " + cursos.size();
    }
}
public class Main {
    public static void main(String[] args) {
        // Crear 2 profesores
        Profesor prof1 = new Profesor("Carlos Mendoza", 45);
        Profesor prof2 = new Profesor("Ana Suarez", 38);

        // Crear 3 estudiantes
        Estudiante est1 = new Estudiante("Renzo Geomar Mamani Quispe", 19);
        Estudiante est2 = new Estudiante("Lucia Fernandez", 20);
        Estudiante est3 = new Estudiante("Mario Vargas", 21);

        // Crear 2 cursos (el horario se crea por composición dentro del curso)
        Curso curso1 = new Curso("Ingeniería de Software", "Lunes y Miércoles", "10:00 - 12:00");
        Curso curso2 = new Curso("Base de Datos", "Martes y Jueves", "14:00 - 16:00");

        // Crear universidad y agregar cursos (Agregación)
        Universidad unsa = new Universidad("UNSA");
        unsa.agregarCurso(curso1);
        unsa.agregarCurso(curso2);

        // Generar reporte de un estudiante (Dependencia)
        Reporte reporte = new Reporte();
        reporte.generarReporteAcademico(est1);
    }
}
class Reporte {
    // El método depende del objeto Estudiante temporalmente para funcionar
    public void generarReporteAcademico(Estudiante estudiante) {
        System.out.println("=== REPORTE GENERADO ===");
        System.out.println("Fecha: " + java.time.LocalDate.now());
        System.out.println("Datos del alumno: " + estudiante.getNombre());
        System.out.println("Edad: " + estudiante.getEdad());
        System.out.println("========================");
    }
}
class Curso {
    private String nombreCurso;
    private Horario horario; // Composición

    public Curso(String nombreCurso, String dias, String horas) {
        this.nombreCurso = nombreCurso;
        // El horario nace y muere con el curso
        this.horario = new Horario(dias, horas);
    }

    public String getNombreCurso() { return nombreCurso; }
    public void setNombreCurso(String nombreCurso) { this.nombreCurso = nombreCurso; }
    public Horario getHorario() { return horario; }
    public void setHorario(Horario horario) { this.horario = horario; }

    @Override
    public String toString() {
        return "Curso: " + nombreCurso + " | Horario: " + horario.toString();
    }
}
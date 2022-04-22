# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from tkinter import CASCADE
from django.db import models


class Acronimo(models.Model):
    idacronimo = models.AutoField(db_column='idAcronimo', primary_key=True)  # Field name made lowercase.
    acronimo = models.CharField(db_column='Acronimo', max_length=8)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Acronimo'


class Cp(models.Model):
    cp = models.IntegerField(primary_key=True)
    fk_mpiodel = models.IntegerField(db_column='fk_MpioDel', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CP'


class Calendario(models.Model):
    fechanolab = models.DateTimeField(db_column='FechaNoLab')  # Field name made lowercase.
    texto = models.CharField(db_column='Texto', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Calendario'


class Cargo(models.Model):
    idcargo = models.AutoField(db_column='idCargo', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    fk_depto = models.ForeignKey('Departamento', models.DO_NOTHING, db_column='fk_Depto')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cargo'


class Catalogo(models.Model):
    clave = models.IntegerField(db_column='Clave')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=20)  # Field name made lowercase.
    espartida = models.BooleanField(db_column='Espartida')  # Field name made lowercase.
    codemp = models.CharField(db_column='Codemp', max_length=20, blank=True, null=True)  # Field name made lowercase.
    descri = models.TextField(db_column='Descri', blank=True, null=True)  # Field name made lowercase.
    texto = models.CharField(db_column='Texto', max_length=40, blank=True, null=True)  # Field name made lowercase.
    unidad = models.CharField(db_column='Unidad', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tipo = models.SmallIntegerField(db_column='Tipo')  # Field name made lowercase.
    costo = models.DecimalField(db_column='Costo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    expins = models.FloatField(blank=True, null=True)
    expinse = models.FloatField(db_column='expinsE', blank=True, null=True)  # Field name made lowercase.
    marca = models.BooleanField(db_column='Marca')  # Field name made lowercase.
    marpre = models.BooleanField(db_column='Marpre')  # Field name made lowercase.
    nivel = models.SmallIntegerField(db_column='Nivel', blank=True, null=True)  # Field name made lowercase.
    nivel1 = models.IntegerField(db_column='Nivel1', blank=True, null=True)  # Field name made lowercase.
    crombo = models.CharField(db_column='Crombo', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ultcal = models.SmallIntegerField(db_column='Ultcal', blank=True, null=True)  # Field name made lowercase.
    tchfij = models.SmallIntegerField(db_column='Tchfij', blank=True, null=True)  # Field name made lowercase.
    costod = models.DecimalField(db_column='CostoD', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    costop = models.DecimalField(db_column='CostoP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    costoa1 = models.DecimalField(db_column='CostoA1', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    costoa2 = models.DecimalField(db_column='CostoA2', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    costoa3 = models.DecimalField(db_column='CostoA3', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    costoa4 = models.DecimalField(db_column='CostoA4', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    costoa5 = models.DecimalField(db_column='CostoA5', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    costoa6 = models.DecimalField(db_column='CostoA6', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    costoa7 = models.DecimalField(db_column='CostoA7', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    costoa8 = models.FloatField(db_column='CostoA8', blank=True, null=True)  # Field name made lowercase.
    costoa9 = models.FloatField(db_column='costoA9', blank=True, null=True)  # Field name made lowercase.
    costoa10 = models.DecimalField(db_column='costoA10', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    costoa11 = models.DecimalField(db_column='costoA11', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    costoa12 = models.DecimalField(db_column='costoA12', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    costoa13 = models.DecimalField(db_column='costoA13', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    referencia = models.CharField(db_column='Referencia', max_length=10, blank=True, null=True)  # Field name made lowercase.
    expinsl = models.SmallIntegerField(db_column='ExpInsl', blank=True, null=True)  # Field name made lowercase.
    ultimaimp = models.SmallIntegerField(db_column='ultimaImp', blank=True, null=True)  # Field name made lowercase.
    codigoaux = models.CharField(db_column='codigoAux', max_length=12, blank=True, null=True)  # Field name made lowercase.
    esbasico = models.BooleanField(db_column='esBasico')  # Field name made lowercase.
    partida = models.CharField(db_column='Partida', max_length=20, blank=True, null=True)  # Field name made lowercase.
    familia = models.CharField(db_column='Familia', max_length=15, blank=True, null=True)  # Field name made lowercase.
    unidadproveedor = models.CharField(db_column='unidadProveedor', max_length=10, blank=True, null=True)  # Field name made lowercase.
    factorconversion = models.FloatField(db_column='factorConversion', blank=True, null=True)  # Field name made lowercase.
    insumointegrado = models.BooleanField(db_column='insumoIntegrado')  # Field name made lowercase.
    codprov = models.CharField(db_column='CodProv', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nombreimagen = models.CharField(db_column='NombreImagen', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fichaid = models.CharField(db_column='FichaId', max_length=20, blank=True, null=True)  # Field name made lowercase.
    codprovmat = models.CharField(db_column='CodProvMat', max_length=20, blank=True, null=True)  # Field name made lowercase.
    procedi = models.CharField(db_column='Procedi', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mtohr = models.DecimalField(db_column='MtoHr', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    rutamatexcel = models.CharField(max_length=255, blank=True, null=True)
    consecutivo = models.IntegerField(db_column='Consecutivo', blank=True, null=True)  # Field name made lowercase.
    volumenminimo = models.FloatField(db_column='VolumenMinimo', blank=True, null=True)  # Field name made lowercase.
    codclasificador = models.CharField(db_column='CodClasificador', max_length=4, blank=True, null=True)  # Field name made lowercase.
    inicio = models.DateTimeField(db_column='Inicio', blank=True, null=True)  # Field name made lowercase.
    fin = models.DateTimeField(db_column='Fin', blank=True, null=True)  # Field name made lowercase.
    moadministracion = models.BooleanField(db_column='MoAdministracion')  # Field name made lowercase.
    descrii = models.TextField(db_column='DescriI', blank=True, null=True)  # Field name made lowercase.
    textoi = models.CharField(db_column='TextoI', max_length=40, blank=True, null=True)  # Field name made lowercase.
    unidadi = models.CharField(db_column='UnidadI', max_length=10, blank=True, null=True)  # Field name made lowercase.
    porcenanticipo = models.FloatField(db_column='porcenAnticipo', blank=True, null=True)  # Field name made lowercase.
    tiempoanticipo = models.SmallIntegerField(db_column='tiempoAnticipo', blank=True, null=True)  # Field name made lowercase.
    tiempocredito = models.SmallIntegerField(db_column='tiempoCredito', blank=True, null=True)  # Field name made lowercase.
    cantidadminimacompra = models.FloatField(db_column='CantidadMinimaCompra', blank=True, null=True)  # Field name made lowercase.
    tiempoentrega = models.IntegerField(db_column='tiempoEntrega', blank=True, null=True)  # Field name made lowercase.
    expinsd = models.FloatField(db_column='expinsD', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Catalogo'


class Clasificacionprov(models.Model):
    idclasprov = models.IntegerField(db_column='idClasProv', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=40)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClasificacionProv'


class Contrato(models.Model):
    idcontrato = models.SmallIntegerField(db_column='idContrato', primary_key=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=60)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Contrato'


class Costohorario(models.Model):
    codigo = models.CharField(max_length=20)
    codva = models.CharField(max_length=20, blank=True, null=True)
    codlla = models.CharField(max_length=20, blank=True, null=True)
    codcomb = models.CharField(max_length=20, blank=True, null=True)
    codacei = models.CharField(db_column='codAcei', max_length=20, blank=True, null=True)  # Field name made lowercase.
    codotrasfuentes = models.CharField(db_column='codOtrasFuentes', max_length=20, blank=True, null=True)  # Field name made lowercase.
    codpza = models.CharField(db_column='codPza', max_length=20, blank=True, null=True)  # Field name made lowercase.
    foper = models.FloatField(blank=True, null=True)
    potencia = models.FloatField(blank=True, null=True)
    ve = models.IntegerField(blank=True, null=True)
    ha = models.IntegerField(blank=True, null=True)
    vr = models.FloatField(blank=True, null=True)
    s = models.FloatField(blank=True, null=True)
    q = models.FloatField(blank=True, null=True)
    interesp = models.FloatField(blank=True, null=True)
    interesd = models.FloatField(blank=True, null=True)
    porintnal = models.FloatField(blank=True, null=True)
    mtodlc = models.FloatField(blank=True, null=True)
    mtonal = models.FloatField(blank=True, null=True)
    mtoafec = models.FloatField(blank=True, null=True)
    costoinactivo = models.DecimalField(db_column='costoInactivo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    factcomb = models.FloatField(blank=True, null=True)
    ccarter = models.FloatField(blank=True, null=True)
    horasc = models.IntegerField(blank=True, null=True)
    faceite = models.FloatField(blank=True, null=True)
    hllantas = models.IntegerField(blank=True, null=True)
    hpiezas = models.IntegerField(db_column='hPiezas', blank=True, null=True)  # Field name made lowercase.
    numserie = models.CharField(db_column='NumSerie', max_length=20, blank=True, null=True)  # Field name made lowercase.
    capacidad = models.CharField(db_column='Capacidad', max_length=25, blank=True, null=True)  # Field name made lowercase.
    vidautil = models.CharField(db_column='VidaUtil', max_length=25, blank=True, null=True)  # Field name made lowercase.
    valorcomercial = models.DecimalField(db_column='ValorComercial', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    disponibilidad = models.CharField(db_column='Disponibilidad', max_length=1, blank=True, null=True)  # Field name made lowercase.
    modelo = models.CharField(db_column='Modelo', max_length=25, blank=True, null=True)  # Field name made lowercase.
    ubicacion = models.CharField(db_column='Ubicacion', max_length=25, blank=True, null=True)  # Field name made lowercase.
    marca = models.CharField(db_column='Marca', max_length=25, blank=True, null=True)  # Field name made lowercase.
    factfuentes = models.FloatField(db_column='factFuentes', blank=True, null=True)  # Field name made lowercase.
    unidadpotencia = models.CharField(db_column='UnidadPotencia', max_length=5, blank=True, null=True)  # Field name made lowercase.
    porvidautil = models.DecimalField(db_column='PorVidaUtil', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    gdfcombustible = models.SmallIntegerField(db_column='GdfCombustible', blank=True, null=True)  # Field name made lowercase.
    gdfgrupo = models.SmallIntegerField(db_column='GdfGrupo', blank=True, null=True)  # Field name made lowercase.
    propietario = models.CharField(db_column='Propietario', max_length=80, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CostoHorario'


class Costosxregion(models.Model):
    idcostosxregion = models.IntegerField(db_column='IdCostosXRegion')  # Field name made lowercase.
    clave = models.IntegerField(db_column='Clave', blank=True, null=True)  # Field name made lowercase.
    region = models.IntegerField(db_column='Region', blank=True, null=True)  # Field name made lowercase.
    costo = models.DecimalField(db_column='Costo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    costo2005 = models.DecimalField(db_column='Costo2005', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CostosXRegion'


class Departamento(models.Model):
    iddepto = models.AutoField(db_column='idDepto', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Departamento'


class Disciplina(models.Model):
    iddisciplina = models.AutoField(db_column='idDisciplina', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    fk_tecinfo = models.IntegerField(db_column='fk_TecInfo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Disciplina'


class Divisionesaec(models.Model):
    iddivaec = models.AutoField(db_column='idDivAec', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DivisionesAec'


class Draftsupplier(models.Model):
    iddraftsup = models.AutoField(db_column='idDraftSup', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'DraftSupplier'


class Empleados(models.Model):
    idempleado = models.AutoField(auto_created=True, db_column='idEmpleado', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=5)  # Field name made lowercase.
    fechaing = models.DateField(db_column='fechaIng')  # Field name made lowercase.
    fechabaja = models.DateField(db_column='fechaBaja', blank=True, null=True)  # Field name made lowercase.
    tipocontrato = models.CharField(db_column='tipoContrato', max_length=25, blank=True, null=True)  # Field name made lowercase.
    sueldomensual = models.FloatField(db_column='sueldoMensual', blank=True, null=True)  # Field name made lowercase.
    referencia1 = models.CharField(db_column='Referencia1', max_length=200, blank=True, null=True)  # Field name made lowercase.
    referencia2 = models.CharField(db_column='Referencia2', max_length=200, blank=True, null=True)  # Field name made lowercase.
    ubicacion = models.CharField(db_column='Ubicacion', max_length=45, blank=True, null=True)  # Field name made lowercase.
    procedencia = models.CharField(db_column='Procedencia', max_length=10, blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fk_cargo = models.ForeignKey('Cargo',db_column='fk_Cargo', on_delete=models.CASCADE,auto_created=True)  # Field name made lowercase.
    fk_personal = models.ForeignKey('Personal',db_column='fk_Personal',auto_created=True, on_delete=models.CASCADE)  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'Empleados'


class Environmentomc(models.Model):
    idenvomc = models.IntegerField(db_column='idEnvOMC', primary_key=True)  # Field name made lowercase.
    number = models.IntegerField()
    eng = models.CharField(max_length=60, blank=True, null=True)
    spa = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EnvironmentOMC'


class Especialidad(models.Model):
    idespecialidad = models.SmallIntegerField(db_column='idEspecialidad', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=250)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Especialidad'


class Especialidadconstruccion(models.Model):
    idespcon = models.AutoField(db_column='idEspCon', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    abreviacion = models.CharField(db_column='Abreviacion', max_length=3, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EspecialidadConstruccion'


class Estado(models.Model):
    idestado = models.AutoField(db_column='idEstado', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=25)  # Field name made lowercase.
    iso = models.CharField(db_column='ISO', max_length=4, blank=True, null=True)  # Field name made lowercase.
    fk_pais = models.IntegerField(db_column='fk_Pais')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Estado'


class Factores(models.Model):
    idfactores = models.IntegerField(db_column='IdFactores')  # Field name made lowercase.
    idunidad1 = models.IntegerField(db_column='IdUnidad1')  # Field name made lowercase.
    factor = models.FloatField(db_column='Factor')  # Field name made lowercase.
    idunidad2 = models.IntegerField(db_column='IdUnidad2')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Factores'


class Familia(models.Model):
    idfamilia = models.SmallIntegerField(db_column='idFamilia', primary_key=True)  # Field name made lowercase.
    codigo = models.IntegerField(db_column='Codigo', blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=50)  # Field name made lowercase.
    fk_especialidad = models.IntegerField(db_column='fk_Especialidad')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Familia'


class Invitado(models.Model):
    idinvitado = models.IntegerField(db_column='idInvitado', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    paterno = models.CharField(db_column='Paterno', max_length=45, blank=True, null=True)  # Field name made lowercase.
    materno = models.CharField(db_column='Materno', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cargo = models.CharField(db_column='Cargo', max_length=60, blank=True, null=True)  # Field name made lowercase.
    cel = models.CharField(db_column='Cel', max_length=12, blank=True, null=True)  # Field name made lowercase.
    orgprocedencia = models.CharField(db_column='orgProcedencia', max_length=60, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=250, blank=True, null=True)  # Field name made lowercase.
    fk_usuario = models.IntegerField(db_column='fk_Usuario', blank=True, null=True)  # Field name made lowercase.
    fk_mundeleg = models.IntegerField(db_column='fk_MunDeleg', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Invitado'


class Marca(models.Model):
    idmarca = models.IntegerField(db_column='idMarca', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    fk_proveedor = models.IntegerField(db_column='fk_Proveedor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Marca'


class Materiales(models.Model):
    idmatcc = models.IntegerField(db_column='idMatcc', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=250)  # Field name made lowercase.
    fk_subfcc = models.IntegerField(db_column='fk_Subfcc')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Materiales'


class Materialshasbrand(models.Model):
    idmatbra = models.IntegerField(db_column='idMatBra', primary_key=True)  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=45)  # Field name made lowercase.
    fk_matcc = models.IntegerField(db_column='fk_Matcc')  # Field name made lowercase.
    fk_brand = models.IntegerField(db_column='fk_Brand', blank=True, null=True)  # Field name made lowercase.
    fk_munits = models.IntegerField(db_column='fk_MUnits')  # Field name made lowercase.
    plist = models.FloatField(db_column='pList', blank=True, null=True)  # Field name made lowercase.
    pmarket = models.FloatField(db_column='pMarket', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MaterialshasBrand'


class Matrices(models.Model):
    clave = models.IntegerField(db_column='Clave')  # Field name made lowercase.
    codigomat = models.CharField(db_column='CodigoMat', max_length=20)  # Field name made lowercase.
    renglon = models.SmallIntegerField(db_column='Renglon')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=20)  # Field name made lowercase.
    operacion = models.CharField(db_column='Operacion', max_length=1)  # Field name made lowercase.
    volumen = models.FloatField(db_column='Volumen')  # Field name made lowercase.
    importep = models.DecimalField(db_column='ImporteP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    imported = models.DecimalField(db_column='ImporteD', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    renglonaux = models.SmallIntegerField(db_column='renglonAux', blank=True, null=True)  # Field name made lowercase.
    renglonsap = models.IntegerField(db_column='RenglonSap', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Matrices'


class Matrizcriterio(models.Model):
    codigo = models.CharField(db_column='Codigo', max_length=20)  # Field name made lowercase.
    criterio = models.CharField(db_column='Criterio', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MatrizCriterio'


class Mftnivel1(models.Model):
    idmftn1 = models.AutoField(db_column='idMftN1', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=6)  # Field name made lowercase.
    descrieng = models.CharField(db_column='descriEng', max_length=80)  # Field name made lowercase.
    descrispa = models.CharField(db_column='descriSpa', max_length=90, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MftNivel1'


class Mftnivel2(models.Model):
    idmftn2 = models.IntegerField(db_column='idMftN2', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=6)  # Field name made lowercase.
    descrieng = models.CharField(db_column='descriEng', max_length=120)  # Field name made lowercase.
    descrispa = models.CharField(db_column='descriSpa', max_length=150, blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fk_mftn1 = models.IntegerField(db_column='fk_MftN1')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MftNivel2'


class Mftnivel3(models.Model):
    idmftn3 = models.IntegerField(db_column='idMftN3', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=10)  # Field name made lowercase.
    descrieng = models.CharField(db_column='descriEng', max_length=120)  # Field name made lowercase.
    descrispa = models.CharField(db_column='descriSpa', max_length=140, blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=100, blank=True, null=True)  # Field name made lowercase.
    tiporegistro = models.CharField(db_column='tipoRegistro', max_length=8, blank=True, null=True)  # Field name made lowercase.
    anioregistro = models.DateField(db_column='anioRegistro', blank=True, null=True)  # Field name made lowercase.
    fk_mftn2 = models.IntegerField(db_column='fk_MftN2')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MftNivel3'


class Mftnivel4(models.Model):
    idmftn4 = models.IntegerField(db_column='idMftN4', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=10)  # Field name made lowercase.
    descrieng = models.CharField(db_column='descriEng', max_length=120)  # Field name made lowercase.
    descrispa = models.CharField(db_column='descriSpa', max_length=130, blank=True, null=True)  # Field name made lowercase.
    tiporegistro = models.CharField(db_column='tipoRegistro', max_length=8, blank=True, null=True)  # Field name made lowercase.
    anioregistro = models.DateField(db_column='anioRegistro', blank=True, null=True)  # Field name made lowercase.
    fk_mftn3 = models.IntegerField(db_column='fk_MftN3')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MftNivel4'


class Mftnivel5(models.Model):
    idmftn5 = models.IntegerField(db_column='idMftN5', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=10)  # Field name made lowercase.
    descrieng = models.CharField(db_column='descriEng', max_length=120)  # Field name made lowercase.
    descrispa = models.CharField(db_column='descriSpa', max_length=140, blank=True, null=True)  # Field name made lowercase.
    tiporegistro = models.CharField(db_column='tipoRegistro', max_length=8, blank=True, null=True)  # Field name made lowercase.
    anioregistro = models.DateField(db_column='anioRegistro', blank=True, null=True)  # Field name made lowercase.
    fk_mftn4 = models.IntegerField(db_column='fk_MftN4')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MftNivel5'


class Mundeleg(models.Model):
    idmundeleg = models.AutoField(db_column='idMunDeleg', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    fk_estado = models.IntegerField(db_column='fk_Estado', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MunDeleg'


class Omc23Nivel1(models.Model):
    idomc23n1 = models.SmallIntegerField(db_column='idOmc23N1', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=10)  # Field name made lowercase.
    descrieng = models.CharField(db_column='descriEng', max_length=100)  # Field name made lowercase.
    descrispa = models.CharField(db_column='descriSpa', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fk_envomc = models.IntegerField(db_column='fk_EnvOmc')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Omc23Nivel1'


class Omc23Nivel2(models.Model):
    idomc23n2 = models.IntegerField(db_column='idOmc23N2', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=10)  # Field name made lowercase.
    descrieng = models.CharField(db_column='descriEng', max_length=100)  # Field name made lowercase.
    descrispa = models.CharField(db_column='descriSpa', max_length=110, blank=True, null=True)  # Field name made lowercase.
    fk_omc23n2 = models.IntegerField(db_column='fk_Omc23N2')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Omc23Nivel2'


class Omc23Nivel3(models.Model):
    idomc23n3 = models.IntegerField(db_column='idOmc23N3', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=10)  # Field name made lowercase.
    descrieng = models.CharField(db_column='descriEng', max_length=100)  # Field name made lowercase.
    descrispa = models.CharField(db_column='descriSpa', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fk_omc23n2 = models.IntegerField(db_column='fk_Omc23N2')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Omc23Nivel3'


class Omc23Nivel4(models.Model):
    idomc23n4 = models.IntegerField(db_column='idOmc23N4', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=15)  # Field name made lowercase.
    descrieng = models.CharField(db_column='descriEng', max_length=100)  # Field name made lowercase.
    descrispa = models.CharField(db_column='descriSpa', max_length=110, blank=True, null=True)  # Field name made lowercase.
    fk_omc23n3 = models.IntegerField(db_column='fk_Omc23N3')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Omc23Nivel4'


class Omc23Nivel5(models.Model):
    idomc23n5 = models.IntegerField(db_column='idOmc23N5', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=15)  # Field name made lowercase.
    descrieng = models.CharField(db_column='descriEng', max_length=120)  # Field name made lowercase.
    descrispa = models.CharField(db_column='descriSpa', max_length=120, blank=True, null=True)  # Field name made lowercase.
    fk_omc23n4 = models.IntegerField(db_column='fk_Omc23N4')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Omc23Nivel5'


class Omc23Nivel6(models.Model):
    idomc23n6 = models.IntegerField(db_column='idOmc23N6', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=18)  # Field name made lowercase.
    descrieng = models.CharField(db_column='descriEng', max_length=100)  # Field name made lowercase.
    descrispa = models.CharField(db_column='descriSpa', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fk_omc23n = models.IntegerField(db_column='fk_Omc23N')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Omc23Nivel6'


class Omc34Nivel1(models.Model):
    idomc34n1 = models.SmallIntegerField(db_column='idOmc34N1', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=9)  # Field name made lowercase.
    descrieng = models.CharField(db_column='descriEng', max_length=30)  # Field name made lowercase.
    descrispa = models.CharField(db_column='descriSpa', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Omc34Nivel1'


class Omc34Nivel2(models.Model):
    idomc34n2 = models.IntegerField(db_column='idOmc34N2', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=9)  # Field name made lowercase.
    descrieng = models.CharField(db_column='descriEng', max_length=35)  # Field name made lowercase.
    descrispa = models.CharField(db_column='descriSpa', max_length=50, blank=True, null=True)  # Field name made lowercase.
    fk_omc34n1 = models.IntegerField(db_column='fk_Omc34N1')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Omc34Nivel2'


class Omc34Nivel3(models.Model):
    idomc34n3 = models.IntegerField(db_column='idOmc34N3', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=13)  # Field name made lowercase.
    descrieng = models.CharField(db_column='descriEng', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descrispa = models.CharField(db_column='descriSpa', max_length=50, blank=True, null=True)  # Field name made lowercase.
    tiporegistro = models.CharField(db_column='tipoRegistro', max_length=8, blank=True, null=True)  # Field name made lowercase.
    origenregistro = models.CharField(db_column='origenRegistro', max_length=45, blank=True, null=True)  # Field name made lowercase.
    anioregistro = models.DateField(db_column='anioRegistro', blank=True, null=True)  # Field name made lowercase.
    fk_omc34n2 = models.IntegerField(db_column='fk_Omc34N2')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Omc34Nivel3'


class Omc34Nivel4(models.Model):
    idomc34n4 = models.IntegerField(db_column='idOmc34N4', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=13)  # Field name made lowercase.
    descrieng = models.CharField(db_column='descriEng', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descrispa = models.CharField(db_column='descriSpa', max_length=65, blank=True, null=True)  # Field name made lowercase.
    tiporegistro = models.CharField(db_column='tipoRegistro', max_length=8, blank=True, null=True)  # Field name made lowercase.
    origenregistro = models.CharField(db_column='origenRegistro', max_length=45, blank=True, null=True)  # Field name made lowercase.
    anioregistro = models.DateField(db_column='anioRegistro', blank=True, null=True)  # Field name made lowercase.
    fk_omc34n3 = models.IntegerField(db_column='fk_Omc34N3')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Omc34Nivel4'


class Omc34Nivel5(models.Model):
    idomc34n5 = models.IntegerField(db_column='idOmc34N5', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=15)  # Field name made lowercase.
    descrieng = models.CharField(db_column='descriEng', max_length=50, blank=True, null=True)  # Field name made lowercase.
    descrispa = models.CharField(db_column='descriSpa', max_length=65, blank=True, null=True)  # Field name made lowercase.
    tiporegistro = models.CharField(db_column='tipoRegistro', max_length=8, blank=True, null=True)  # Field name made lowercase.
    origenregistro = models.CharField(db_column='origenRegistro', max_length=45, blank=True, null=True)  # Field name made lowercase.
    anioregistro = models.DateField(db_column='anioRegistro', blank=True, null=True)  # Field name made lowercase.
    fk_omc34n4 = models.IntegerField(db_column='fk_Omc34N4')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Omc34Nivel5'


class Omc35Nivel1(models.Model):
    idomc35n1 = models.SmallIntegerField(db_column='idOmc35N1', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=9)  # Field name made lowercase.
    descrieng = models.CharField(db_column='descriEng', max_length=30)  # Field name made lowercase.
    descrispa = models.CharField(db_column='descriSpa', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fk_envomc = models.IntegerField(db_column='fk_EnvOMC')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Omc35Nivel1'


class Omc35Nivel2(models.Model):
    idomc35n2 = models.IntegerField(db_column='idOmc35N2', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=9)  # Field name made lowercase.
    descrieng = models.CharField(db_column='descriEng', max_length=50)  # Field name made lowercase.
    descrispa = models.CharField(db_column='descriSpa', max_length=80, blank=True, null=True)  # Field name made lowercase.
    fk_omc35n1 = models.IntegerField(db_column='fk_Omc35N1')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Omc35Nivel2'


class Omc35Nivel3(models.Model):
    idomc35n3 = models.IntegerField(db_column='idOmc35N3', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=9)  # Field name made lowercase.
    descrieng = models.CharField(db_column='descriEng', max_length=60)  # Field name made lowercase.
    descrispa = models.CharField(db_column='descriSpa', max_length=80, blank=True, null=True)  # Field name made lowercase.
    fk_omc35n2 = models.IntegerField(db_column='fk_Omc35N2')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Omc35Nivel3'


class Omc35Nivel4(models.Model):
    idomc35n4 = models.IntegerField(db_column='idOmc35N4', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=15)  # Field name made lowercase.
    descrieng = models.CharField(db_column='descriEng', max_length=80)  # Field name made lowercase.
    descrispa = models.CharField(db_column='descriSpa', max_length=90, blank=True, null=True)  # Field name made lowercase.
    fk_omc35n3 = models.IntegerField(db_column='fk_Omc35N3')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Omc35Nivel4'


class Omc35Nivel5(models.Model):
    idomc35n5 = models.IntegerField(db_column='idOmc35N5', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=18)  # Field name made lowercase.
    descrieng = models.CharField(db_column='descriEng', max_length=90)  # Field name made lowercase.
    descrispa = models.CharField(db_column='descriSpa', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fk_omc35n4 = models.IntegerField(db_column='fk_Omc35N4')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Omc35Nivel5'


class Omc35Nivel6(models.Model):
    idomc35n6 = models.IntegerField(db_column='idOmc35N6', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=20)  # Field name made lowercase.
    descrieng = models.CharField(db_column='descriEng', max_length=75)  # Field name made lowercase.
    descrispa = models.CharField(db_column='descriSpa', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fk_omc35n5 = models.IntegerField(db_column='fk_Omc35N5')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Omc35Nivel6'


class Omc41Nivel1(models.Model):
    idomc41n1 = models.IntegerField(db_column='idOmc41N1', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=9)  # Field name made lowercase.
    nombreeng = models.CharField(db_column='nombreEng', max_length=25)  # Field name made lowercase.
    nombrespa = models.CharField(db_column='nombreSpa', max_length=25, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Omc41Nivel1'


class Omc41Nivel2(models.Model):
    idomc41n2 = models.IntegerField(db_column='idOmc41N2', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=9)  # Field name made lowercase.
    nombreeng = models.CharField(db_column='nombreEng', max_length=35)  # Field name made lowercase.
    nombrespa = models.CharField(db_column='nombreSpa', max_length=35, blank=True, null=True)  # Field name made lowercase.
    fk_omc41n1 = models.IntegerField(db_column='fk_Omc41N1')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Omc41Nivel2'


class Omc41Nivel3(models.Model):
    idomc41n3 = models.IntegerField(db_column='idOmc41N3', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=9)  # Field name made lowercase.
    nombreeng = models.CharField(db_column='nombreEng', max_length=40)  # Field name made lowercase.
    nombrespa = models.CharField(db_column='nombreSpa', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fk_omc41n2 = models.IntegerField(db_column='fk_Omc41N2')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Omc41Nivel3'


class Omc41Nivel4(models.Model):
    idomc41n4 = models.IntegerField(db_column='idOmc41N4', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=11)  # Field name made lowercase.
    nombreeng = models.CharField(db_column='nombreEng', max_length=50)  # Field name made lowercase.
    nombrespa = models.CharField(db_column='nombreSpa', max_length=55, blank=True, null=True)  # Field name made lowercase.
    fk_omc41n3 = models.IntegerField(db_column='fk_Omc41N3')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Omc41Nivel4'


class Omc41Nivel5(models.Model):
    idomc41n5 = models.IntegerField(db_column='idOmc41N5', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=13)  # Field name made lowercase.
    nombreeng = models.CharField(db_column='nombreEng', max_length=35)  # Field name made lowercase.
    nombrespa = models.CharField(db_column='nombreSpa', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fk_omc41n4 = models.IntegerField(db_column='fk_Omc41N4')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Omc41Nivel5'


class Omc41Nivel6(models.Model):
    idomc41n6 = models.IntegerField(db_column='idOmc41N6', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=15)  # Field name made lowercase.
    nombreeng = models.CharField(db_column='nombreEng', max_length=30)  # Field name made lowercase.
    nombrespa = models.CharField(db_column='nombreSpa', max_length=30, blank=True, null=True)  # Field name made lowercase.
    fk_omc41n5 = models.IntegerField(db_column='fk_Omc41N5')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Omc41Nivel6'


class Pais(models.Model):
    idpais = models.AutoField(db_column='idPais', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    iso = models.CharField(db_column='ISO', max_length=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pais'


class Parametros(models.Model):
    parametro = models.CharField(db_column='Parametro', max_length=25)  # Field name made lowercase.
    valor = models.CharField(db_column='Valor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    explicacion = models.CharField(db_column='Explicacion', max_length=75, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Parametros'


class Partida(models.Model):
    idpartida = models.AutoField(db_column='idPartida', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=90)  # Field name made lowercase.
    fk_espcon = models.IntegerField(db_column='fk_EspCon')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Partida'


class Personal(models.Model):
    idpersonal = models.IntegerField(db_column='idPersonal', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45, blank=True, null=True)  # Field name made lowercase.
    paterno = models.CharField(db_column='Paterno', max_length=45, blank=True, null=True)  # Field name made lowercase.
    materno = models.CharField(db_column='Materno', max_length=45, blank=True, null=True)  # Field name made lowercase.
    genero = models.CharField(db_column='Genero', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fechanac = models.DateField(db_column='fechaNac', blank=True, null=True)  # Field name made lowercase.
    lugarnac = models.CharField(db_column='lugarNac', max_length=45, blank=True, null=True)  # Field name made lowercase.
    rfc = models.CharField(db_column='RFC', max_length=13, blank=True, null=True)  # Field name made lowercase.
    curp = models.CharField(db_column='CURP', max_length=18, blank=True, null=True)  # Field name made lowercase.
    cel = models.CharField(db_column='Cel', max_length=12, blank=True, null=True)  # Field name made lowercase.
    calle = models.CharField(db_column='Calle', max_length=45, blank=True, null=True)  # Field name made lowercase.
    noint = models.IntegerField(db_column='noInt', blank=True, null=True)  # Field name made lowercase.
    noext = models.IntegerField(db_column='noExt', blank=True, null=True)  # Field name made lowercase.
    fk_usuario = models.IntegerField(db_column='fk_Usuario', blank=True, null=True)  # Field name made lowercase.
    fk_mundeleg = models.IntegerField(db_column='fk_MunDeleg', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Personal'


class Presupuesto(models.Model):
    clave = models.IntegerField(db_column='Clave')  # Field name made lowercase.
    partida = models.CharField(db_column='Partida', max_length=20)  # Field name made lowercase.
    renglon = models.IntegerField(db_column='Renglon')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=20)  # Field name made lowercase.
    cantidad = models.FloatField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.
    indirl = models.BooleanField(db_column='IndirL')  # Field name made lowercase.
    indirm = models.FloatField(db_column='IndirM', blank=True, null=True)  # Field name made lowercase.
    marca = models.BooleanField(db_column='Marca')  # Field name made lowercase.
    renglonaux = models.IntegerField(db_column='RenglonAux', blank=True, null=True)  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    total = models.DecimalField(db_column='Total', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    porcen = models.FloatField(db_column='Porcen', blank=True, null=True)  # Field name made lowercase.
    preciop = models.DecimalField(db_column='PrecioP', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    preciod = models.DecimalField(db_column='PrecioD', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    codemp = models.CharField(db_column='Codemp', max_length=20, blank=True, null=True)  # Field name made lowercase.
    descri = models.TextField(db_column='Descri', blank=True, null=True)  # Field name made lowercase.
    rendim = models.FloatField(db_column='Rendim', blank=True, null=True)  # Field name made lowercase.
    cuenta = models.CharField(db_column='Cuenta', max_length=20, blank=True, null=True)  # Field name made lowercase.
    crombo = models.CharField(db_column='Crombo', max_length=2, blank=True, null=True)  # Field name made lowercase.
    estaes = models.FloatField(db_column='EstaEs', blank=True, null=True)  # Field name made lowercase.
    acumul = models.FloatField(db_column='Acumul', blank=True, null=True)  # Field name made lowercase.
    totact = models.DecimalField(db_column='TotAct', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totacu = models.DecimalField(db_column='TotAcu', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    tmpest = models.FloatField(db_column='TmpEst', blank=True, null=True)  # Field name made lowercase.
    tmppor = models.FloatField(db_column='TmpPor', blank=True, null=True)  # Field name made lowercase.
    codigoprima = models.CharField(db_column='codigoPrima', max_length=25, blank=True, null=True)  # Field name made lowercase.
    porcen2 = models.FloatField(db_column='Porcen2', blank=True, null=True)  # Field name made lowercase.
    contrato1 = models.BooleanField(db_column='Contrato1')  # Field name made lowercase.
    contrato2 = models.BooleanField(db_column='Contrato2')  # Field name made lowercase.
    contrato3 = models.BooleanField(db_column='Contrato3')  # Field name made lowercase.
    contrato4 = models.BooleanField(db_column='Contrato4')  # Field name made lowercase.
    contrato5 = models.BooleanField(db_column='Contrato5')  # Field name made lowercase.
    contrato6 = models.BooleanField(db_column='Contrato6')  # Field name made lowercase.
    contrato7 = models.BooleanField(db_column='Contrato7')  # Field name made lowercase.
    contrato8 = models.BooleanField(db_column='Contrato8')  # Field name made lowercase.
    contrato9 = models.BooleanField(db_column='Contrato9')  # Field name made lowercase.
    totaldestajo = models.DecimalField(db_column='TotalDestajo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fechaini = models.DateTimeField(db_column='FechaIni', blank=True, null=True)  # Field name made lowercase.
    fechafin = models.DateTimeField(db_column='FechaFin', blank=True, null=True)  # Field name made lowercase.
    duracion = models.SmallIntegerField(db_column='Duracion', blank=True, null=True)  # Field name made lowercase.
    totalprograma = models.DecimalField(db_column='TotalPrograma', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    calculoruta = models.BooleanField(db_column='CalculoRuta')  # Field name made lowercase.
    posx = models.FloatField(db_column='PosX', blank=True, null=True)  # Field name made lowercase.
    posy = models.FloatField(db_column='PosY', blank=True, null=True)  # Field name made lowercase.
    nivel = models.FloatField(db_column='Nivel', blank=True, null=True)  # Field name made lowercase.
    actividadcritica = models.BooleanField(db_column='ActividadCritica')  # Field name made lowercase.
    holgura = models.IntegerField(db_column='Holgura', blank=True, null=True)  # Field name made lowercase.
    fechainitardia = models.DateTimeField(db_column='FechaIniTardia', blank=True, null=True)  # Field name made lowercase.
    fechafintardia = models.DateTimeField(db_column='FechaFinTardia', blank=True, null=True)  # Field name made lowercase.
    codresp = models.CharField(db_column='CodResp', max_length=10, blank=True, null=True)  # Field name made lowercase.
    expandir = models.SmallIntegerField(db_column='Expandir', blank=True, null=True)  # Field name made lowercase.
    pexpandir = models.BooleanField(db_column='PExpandir')  # Field name made lowercase.
    padre = models.CharField(db_column='Padre', max_length=20, blank=True, null=True)  # Field name made lowercase.
    inicioreal = models.DateTimeField(db_column='InicioReal', blank=True, null=True)  # Field name made lowercase.
    finreal = models.DateTimeField(db_column='FinReal', blank=True, null=True)  # Field name made lowercase.
    avance = models.DecimalField(db_column='Avance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    codigosap2005 = models.CharField(db_column='CodigoSap2005', max_length=60, blank=True, null=True)  # Field name made lowercase.
    continua = models.BooleanField(db_column='Continua')  # Field name made lowercase.
    neco = models.CharField(db_column='Neco', max_length=20, blank=True, null=True)  # Field name made lowercase.
    codsupervisor = models.CharField(db_column='CodSupervisor', max_length=10, blank=True, null=True)  # Field name made lowercase.
    codigovivienda = models.IntegerField(db_column='CodigoVivienda', blank=True, null=True)  # Field name made lowercase.
    imsssari = models.DecimalField(db_column='ImssSarI', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    formatogenerador = models.CharField(db_column='FormatoGenerador', max_length=255, blank=True, null=True)  # Field name made lowercase.
    seestima = models.BooleanField(db_column='SeEstima')  # Field name made lowercase.
    comentarios = models.TextField(db_column='Comentarios', blank=True, null=True)  # Field name made lowercase.
    comentariosi = models.TextField(db_column='ComentariosI', blank=True, null=True)  # Field name made lowercase.
    descrii = models.TextField(db_column='DescriI', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Presupuesto'


class Proveedor(models.Model):
    idproveedor = models.AutoField(db_column='idProveedor', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=60)  # Field name made lowercase.
    rfc = models.CharField(db_column='RFC', max_length=45, blank=True, null=True)  # Field name made lowercase.
    calle = models.CharField(db_column='Calle', max_length=50, blank=True, null=True)  # Field name made lowercase.
    noint = models.IntegerField(db_column='noInt', blank=True, null=True)  # Field name made lowercase.
    noext = models.IntegerField(db_column='noExt', blank=True, null=True)  # Field name made lowercase.
    colonia = models.CharField(db_column='Colonia', max_length=50, blank=True, null=True)  # Field name made lowercase.
    numerotel = models.CharField(db_column='numeroTel', max_length=20, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=30, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45, blank=True, null=True)  # Field name made lowercase.
    contactoatencion = models.CharField(db_column='contactoAtencion', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nombresuperior = models.CharField(db_column='nombreSuperior', max_length=50, blank=True, null=True)  # Field name made lowercase.
    posicionjefe = models.CharField(db_column='posicionJefe', max_length=45, blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=500, blank=True, null=True)  # Field name made lowercase.
    logoimg = models.CharField(db_column='logoImg', max_length=500, blank=True, null=True)  # Field name made lowercase.
    urlsitioweb = models.CharField(db_column='urlSitioWeb', max_length=70, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Proveedor'


class Repexplosioninsumos(models.Model):
    codigo = models.CharField(db_column='Codigo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    texto = models.CharField(db_column='Texto', max_length=40, blank=True, null=True)  # Field name made lowercase.
    unidad = models.CharField(db_column='Unidad', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tipo = models.SmallIntegerField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    costo = models.DecimalField(db_column='Costo', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateTimeField(db_column='Fecha', blank=True, null=True)  # Field name made lowercase.
    cantidad = models.FloatField(blank=True, null=True)
    importe = models.FloatField(db_column='Importe', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RepExplosionInsumos'


class Reppresupuesto(models.Model):
    partida = models.CharField(db_column='Partida', max_length=20, blank=True, null=True)  # Field name made lowercase.
    renglon = models.IntegerField(db_column='Renglon', blank=True, null=True)  # Field name made lowercase.
    textopartida = models.CharField(db_column='TextoPartida', max_length=40, blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    texto = models.CharField(db_column='Texto', max_length=40, blank=True, null=True)  # Field name made lowercase.
    unidad = models.CharField(db_column='Unidad', max_length=10, blank=True, null=True)  # Field name made lowercase.
    tipo = models.SmallIntegerField(db_column='Tipo', blank=True, null=True)  # Field name made lowercase.
    precio = models.DecimalField(db_column='Precio', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    cantidad = models.FloatField(db_column='Cantidad', blank=True, null=True)  # Field name made lowercase.
    importe = models.DecimalField(max_digits=19, decimal_places=4, blank=True, null=True)
    porcentaje = models.FloatField(db_column='Porcentaje', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RepPresupuesto'


class Reportesejecutivos(models.Model):
    idreporte = models.IntegerField(db_column='idReporte')  # Field name made lowercase.
    idgrupo = models.IntegerField(db_column='idGrupo')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=20)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=40, blank=True, null=True)  # Field name made lowercase.
    nombrevista = models.CharField(db_column='nombreVista', max_length=40)  # Field name made lowercase.
    sentenciaconsulta = models.CharField(db_column='SentenciaConsulta', max_length=255)  # Field name made lowercase.
    documentoexcel = models.CharField(db_column='DocumentoExcel', max_length=255)  # Field name made lowercase.
    hojadatos = models.CharField(db_column='HojaDatos', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReportesEjecutivos'


class Reportesejecutivostdinamicas(models.Model):
    idreportetabladinamica = models.IntegerField(db_column='idReporteTablaDinamica')  # Field name made lowercase.
    idreporte = models.IntegerField(db_column='idReporte')  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReportesEjecutivosTDinamicas'


class Rfafamiliacat1(models.Model):
    idrfafcat1 = models.SmallIntegerField(db_column='idRfaFcat1', primary_key=True)  # Field name made lowercase.
    nombreeng = models.CharField(db_column='nombreEng', max_length=30)  # Field name made lowercase.
    nombrespa = models.CharField(db_column='nombreSpa', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RfaFamiliaCat1'


class Rfafamiliacat2(models.Model):
    idrfafcat2 = models.IntegerField(db_column='idRfaFcat2', primary_key=True)  # Field name made lowercase.
    nombreeng = models.CharField(db_column='nombreEng', max_length=60)  # Field name made lowercase.
    nombrespa = models.CharField(db_column='nombreSpa', max_length=60, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=45)  # Field name made lowercase.
    fk_rfafcat1 = models.IntegerField(db_column='fk_RfaFcat1')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RfaFamiliaCat2'


class Rfafamiliacat3(models.Model):
    idrfafcat3 = models.IntegerField(db_column='idRfaFcat3', primary_key=True)  # Field name made lowercase.
    nombreeng = models.CharField(db_column='nombreEng', max_length=80)  # Field name made lowercase.
    nombrespa = models.CharField(db_column='nombreSpa', max_length=100, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=45)  # Field name made lowercase.
    fk_rfafcat2 = models.IntegerField(db_column='fk_RfaFcat2')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RfaFamiliaCat3'


class Rfafamiliacat4(models.Model):
    idrfafcat4 = models.IntegerField(db_column='idRfaFcat4', primary_key=True)  # Field name made lowercase.
    nombreeng = models.CharField(db_column='nombreEng', max_length=70)  # Field name made lowercase.
    nombrespa = models.CharField(db_column='nombreSpa', max_length=80, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=45)  # Field name made lowercase.
    fk_rfafcat3 = models.IntegerField(db_column='fk_RfaFcat3')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RfaFamiliaCat4'


class Rfafamiliacat5(models.Model):
    idrfafcat5 = models.IntegerField(db_column='idRfaFcat5', primary_key=True)  # Field name made lowercase.
    nombreeng = models.CharField(db_column='nombreEng', max_length=80)  # Field name made lowercase.
    nombrespa = models.CharField(db_column='nombreSpa', max_length=100, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=45)  # Field name made lowercase.
    fk_rfafcat4 = models.IntegerField(db_column='fk_RfaFcat4')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RfaFamiliaCat5'


class Rfafamiliacat6(models.Model):
    idrfafcat6 = models.IntegerField(db_column='idRfaFcat6', primary_key=True)  # Field name made lowercase.
    nombreeng = models.CharField(db_column='nombreEng', max_length=70)  # Field name made lowercase.
    nombrespa = models.CharField(db_column='nombreSpa', max_length=85, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=45)  # Field name made lowercase.
    fk_rfafcat5 = models.IntegerField(db_column='fk_RfaFcat5')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RfaFamiliaCat6'


class Rfafamiliacat7(models.Model):
    idrfafcat7 = models.IntegerField(db_column='idRfaFcat7', primary_key=True)  # Field name made lowercase.
    nombreeng = models.CharField(db_column='nombreEng', max_length=70)  # Field name made lowercase.
    nombrespa = models.CharField(db_column='nombreSpa', max_length=85, blank=True, null=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=45)  # Field name made lowercase.
    fk_rfafcat6 = models.IntegerField(db_column='fk_RfaFcat6')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RfaFamiliaCat7'


class Rvtgroupparams(models.Model):
    idrvtgp = models.IntegerField(db_column='idRvtgp', primary_key=True)  # Field name made lowercase.
    eng = models.CharField(db_column='Eng', max_length=25, blank=True, null=True)  # Field name made lowercase.
    spa = models.CharField(db_column='Spa', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RvtGroupParams'


class Serviciosaec(models.Model):
    idservaec = models.SmallIntegerField(db_column='idServAec', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=45)  # Field name made lowercase.
    fk_divaec = models.IntegerField(db_column='fk_DivAec')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ServiciosAec'


class Subfamilia(models.Model):
    idsubfamilia = models.IntegerField(db_column='idSubfamilia', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=70)  # Field name made lowercase.
    fk_acronimo = models.IntegerField(db_column='fk_Acronimo', blank=True, null=True)  # Field name made lowercase.
    fk_familia = models.IntegerField(db_column='fk_Familia')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Subfamilia'


class Uftcategorias(models.Model):
    iduftcat = models.AutoField(db_column='idUftCat', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=1)  # Field name made lowercase.
    descrieng = models.CharField(db_column='descriEng', max_length=45, blank=True, null=True)  # Field name made lowercase.
    descrispa = models.CharField(db_column='descriSpa', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UftCategorias'


class Uftnivel2(models.Model):
    iduftn2 = models.IntegerField(db_column='idUftN2', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=3)  # Field name made lowercase.
    descrieng = models.CharField(db_column='descriEng', max_length=70)  # Field name made lowercase.
    descrispa = models.CharField(db_column='descriSpa', max_length=70)  # Field name made lowercase.
    explicacioneng = models.CharField(db_column='explicacionEng', max_length=70, blank=True, null=True)  # Field name made lowercase.
    explicacionspa = models.CharField(db_column='explicacionSpa', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fk_uftcat = models.IntegerField(db_column='fk_UftCat')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UftNivel2'


class Uftnivel3(models.Model):
    iduftn3 = models.IntegerField(db_column='idUftN3', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=5)  # Field name made lowercase.
    descrieng = models.CharField(db_column='descriEng', max_length=150)  # Field name made lowercase.
    descrispa = models.CharField(db_column='descriSpa', max_length=150)  # Field name made lowercase.
    explicacioneng = models.CharField(db_column='explicacionEng', max_length=700, blank=True, null=True)  # Field name made lowercase.
    explicacionspa = models.CharField(db_column='explicacionSpa', max_length=800, blank=True, null=True)  # Field name made lowercase.
    observaciones = models.CharField(db_column='Observaciones', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fk_uftn2 = models.IntegerField(db_column='fk_UftN2', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UftNivel3'


class Uftnivel4(models.Model):
    iduftn4 = models.IntegerField(db_column='idUftN4', primary_key=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=8)  # Field name made lowercase.
    descrieng = models.CharField(db_column='descriEng', max_length=200)  # Field name made lowercase.
    descrispa = models.CharField(db_column='descriSpa', max_length=200)  # Field name made lowercase.
    explicacioneng = models.TextField(db_column='explicacionEng', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    explicacionspa = models.TextField(db_column='explicacionSpa', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    observaciones = models.CharField(db_column='Observaciones', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fk_uftn3 = models.IntegerField(db_column='fk_UftN3')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UftNivel4'


class Unidadesmedida(models.Model):
    idunimed = models.IntegerField(db_column='idUniMed', primary_key=True)  # Field name made lowercase.
    sistema = models.CharField(db_column='Sistema', max_length=60, blank=True, null=True)  # Field name made lowercase.
    unidad = models.CharField(db_column='Unidad', max_length=10)  # Field name made lowercase.
    descripcion = models.CharField(db_column='Descripcion', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UnidadesMedida'


class Usuario(models.Model):
    idusuario = models.AutoField(db_column='idUsuario', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', unique=True, max_length=50, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rol = models.CharField(db_column='Rol', max_length=15, blank=True, null=True)  # Field name made lowercase.
    fechacreacion = models.DateTimeField(db_column='fechaCreacion', blank=True, null=True)  # Field name made lowercase.
    fechaact = models.DateTimeField(db_column='fechaAct')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Usuario'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Porfin(models.Model):
    noperiodo = models.SmallIntegerField(db_column='NoPeriodo')  # Field name made lowercase.
    totcosto = models.DecimalField(db_column='totCosto', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totprecio = models.DecimalField(db_column='totPrecio', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totcostoma = models.DecimalField(db_column='totCostoMA', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totcostomo = models.DecimalField(db_column='totCostoMO', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totcostoeq = models.DecimalField(db_column='totCostoEQ', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'porFin'

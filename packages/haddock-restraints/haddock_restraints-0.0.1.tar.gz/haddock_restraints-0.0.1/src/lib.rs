use std::io::BufReader;

use haddock_restraints::{Air, Interactor};
use pdbtbx::PDB;
use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;

#[pyclass]
pub struct PyInteractor {
    inner: Interactor,
}

#[pymethods]
impl PyInteractor {
    #[new]
    fn new(id: u16, chain: String, active: Vec<i16>, passive: Vec<i16>) -> Self {
        let mut interactor = Interactor::new(id);
        interactor.set_chain(&chain);
        interactor.set_active(active);
        interactor.set_passive(passive);
        PyInteractor { inner: interactor }
    }

    fn set_target(&mut self, target: u16) {
        self.inner.add_target(target)
    }

    fn id(&self) -> u16 {
        self.inner.id()
    }

    fn set_active(&mut self, active: Vec<i16>) {
        self.inner.set_active(active);
    }

    fn set_active_atoms(&mut self, atoms: Vec<String>) {
        self.inner.set_active_atoms(atoms);
    }

    fn set_chain(&mut self, chain: &str) {
        self.inner.set_chain(chain);
    }

    fn set_lower_margin(&mut self, margin: f64) {
        self.inner.set_lower_margin(margin)
    }

    fn set_passive(&mut self, passive: Vec<i16>) {
        self.inner.set_passive(passive);
    }

    fn set_pdb(&mut self, pdb_path: &str) -> PyResult<()> {
        match path_to_pdb(pdb_path) {
            Some(pdb) => {
                self.inner.set_pdb(pdb);
                Ok(())
            }
            None => Err(PyValueError::new_err(
                "Failed to parse PDB: Invalid PDB data.",
            )),
        }
    }

    fn set_surface_as_passive(&mut self) {
        self.inner.set_surface_as_passive();
    }

    fn set_target_distance(&mut self, distance: f64) {
        self.inner.set_target_distance(distance);
    }

    fn set_upper_margin(&mut self, margin: f64) {
        self.inner.set_upper_margin(margin);
    }

    fn set_passive_atoms(&mut self, atoms: Vec<String>) {
        self.inner.set_passive_atoms(atoms);
    }

    fn set_passive_from_active(&mut self) {
        self.inner.set_passive_from_active();
    }

    fn remove_buried_residues(&mut self) {
        self.inner.remove_buried_residues();
    }

    fn set_filter_buried_cutoff(&mut self, cutoff: f64) {
        self.inner.set_filter_buried_cutoff(cutoff);
    }
}

#[pyclass]
pub struct PyAir {
    inner: Air,
}

#[pymethods]
impl PyAir {
    #[new]
    fn new(interactors: Vec<PyRef<PyInteractor>>) -> Self {
        PyAir {
            inner: Air::new(interactors.into_iter().map(|c| c.inner.clone()).collect()),
        }
    }

    fn gen_tbl(&self) -> String {
        match self.inner.gen_tbl() {
            Ok(r) => r,
            Err(r) => r.to_string(),
        }
    }
}

#[pyfunction]
fn restraint_bodies(pdb_path: &str) -> PyResult<String> {
    match path_to_pdb(pdb_path) {
        Some(pdb) => match haddock_restraints::restraint_bodies(pdb, &None) {
            Ok(tbl) => Ok(tbl),
            Err(e) => Err(PyValueError::new_err(format!(
                "Failed to generate restraint bodies: {}",
                e
            ))),
        },
        None => Err(PyValueError::new_err(
            "Failed to generate restraint bodies: Invalid PDB data.",
        )),
    }
}

fn path_to_pdb(path: &str) -> Option<PDB> {
    let buf = std::fs::File::open(path).ok().map(BufReader::new)?;
    let mut opts = pdbtbx::ReadOptions::new();
    opts.set_format(pdbtbx::Format::Pdb)
        .set_level(pdbtbx::StrictnessLevel::Loose);

    opts.read_raw(buf).ok().map(|(pdb, _)| pdb)
}

#[pymodule]
fn _internal(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<PyInteractor>()?;
    m.add_class::<PyAir>()?;
    m.add_function(wrap_pyfunction!(restraint_bodies, m)?)?;
    Ok(())
}

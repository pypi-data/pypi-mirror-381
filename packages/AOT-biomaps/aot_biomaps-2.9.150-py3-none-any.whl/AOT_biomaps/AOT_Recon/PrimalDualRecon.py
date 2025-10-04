from AOT_biomaps.AOT_Recon.AlgebraicRecon import AlgebraicRecon
from AOT_biomaps.AOT_Recon.ReconEnums import ReconType, ProcessType, NoiseType
from AOT_biomaps.AOT_Recon.AOT_Optimizers.PDHG import CP

class PrimalDualRecon(AlgebraicRecon):
    """
    This class implements the convex reconstruction process.
    It currently does not perform any operations but serves as a template for future implementations.
    """
    def __init__(self, alpha, theta=1.0, L=None, noiseModel = NoiseType.GAUSSIAN,**kwargs):
        super().__init__(**kwargs)
        self.reconType = ReconType.Convex
        self.alpha = alpha # regularization parameter
        self.theta = theta # relaxation parameter (between 1 and 2)
        self.L = L # norme spectrale de l'opérateur linéaire défini par les matrices P et P^T
        self.noiseModel = noiseModel

    def run(self, processType=ProcessType.PYTHON, withTumor=True):
        """
        This method is a placeholder for the convex reconstruction process.
        It currently does not perform any operations but serves as a template for future implementations.
        """
        if(processType == ProcessType.CASToR):
            self._convexReconCASToR(withTumor)
        elif(processType == ProcessType.PYTHON):
            self._convexReconPython(withTumor)
        else:
            raise ValueError(f"Unknown convex reconstruction type: {processType}")

    def _convexReconCASToR(self, withTumor):
        pass

    def _convexReconPython(self, withTumor):
        if withTumor:
            self.reconPhantom = CP(
                self.SMatrix, 
                y=self.experiment.AOsignal_withTumor, 
                alpha=self.alpha, 
                theta=self.theta, 
                numIterations=self.numIterations, 
                isSavingEachIteration=self.isSavingEachIteration,
                noiseModel=self.noiseModel,
                L=self.L, 
                withTumor=withTumor,
                device=None
                )
        else:
            self.reconLaser = CP(
                self.SMatrix, 
                y=self.experiment.AOsignal_withoutTumor, 
                alpha=self.alpha, 
                theta=self.theta, 
                numIterations=self.numIterations, 
                isSavingEachIteration=self.isSavingEachIteration,
                noiseModel=self.noiseModel,
                L=self.L, 
                withTumor=withTumor,
                device=None
                )
            



   

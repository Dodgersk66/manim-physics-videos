from manimlib.imports import *

class threeDimensionSceneTest(ThreeDScene):
    def construct(self):
        cylinder = ParametricSurface(self.cylinderFunc,u_min = 0, u_max = TAU, v_min = -2,v_max = 2)
        block = Dot(np.array((-2.0,0.,0.)))

        centrifugalForceVector = Arrow(np.array((-2.,0.,0.)),np.array((-1.5,0.,0.)))

        block.rotate(PI/2,np.array((-2.0,0.,0.)))

        self.set_camera_orientation(phi = PI/3, theta = PI/3,distance=5)
        
        def update_curve(d,dt):
            d.rotate(dt,Y_AXIS)

        block.add_updater(update_curve)
        cylinder.add_updater(update_curve)
        #centrifugalForceVector.add_updater(update_curve)
        self.add(cylinder)
        self.add(block)
        self.add(centrifugalForceVector)
        self.wait(2*PI)

        # self.add(cylinder)
        # self.play(Rotate(cylinder,angle=TAU,axis=Y_AXIS),rate_func=linear)
        # cylinder.rotate_about_origin

    def cylinderFunc(self,u,v):
       return np.array([
           2*np.sin(u),
           v,
           2*np.cos(u)
       ]) 
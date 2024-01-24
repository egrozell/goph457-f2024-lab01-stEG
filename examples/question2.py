import numpy as np

def main():
#  question 2 i
    r = 2.48#e
    r_eps_a = 0.02#e
    h = 10.1#e
    h_eps_a = 0.03#e
    a = np.pi*r**2
    a_max_error= np.abs(2)*np.pi*np.abs(r_eps_a/r)
    a_mpe= np.sqrt((np.pi*r*2)**2*(r_eps_a)**2)
    a_eps_a= r_eps_a+h_eps_a
    v = a*h
    v_max_error = a_max_error + np.abs(h_eps_a/h)
    v_mpe= np.sqrt((((np.pi*r*h*2)**2)*(r_eps_a)**2)+((np.pi*r*2)**2)*(r_eps_a)**2)
    vn = 217 
    vn_eps_a = 8
    vt = vn +v 
    vt_max_error = vn_eps_a + (v_max_error*a)
    vt_mpe = np.sqrt((vn_eps_a)**2 + (v_mpe*a)**2)

    print (f"""
    Area:                       {a}
        Relative Error:
            Max error           {(a_max_error)*100} %
            Most Probable Error {(a_mpe)*100} %
        Absolute Error: 
            Max error           {a_max_error*a} cm^2 
            Most Probable Error {a_mpe*a} cm^2

    Volume:                     {v}
        Relative Error:
            Max error           {(v_max_error)*100} %
            Most Probable Error {(v_mpe)*100} %
        Absolute Error: 
            Max error           {v_max_error*a} cm^3 
            Most Probable Error {v_mpe*a} cm^3
    Volume For Both Cylinders:  {vt} cm^3
        Relative Error:
            Max error           {(vt_max_error)*100} %
            Most Probable Error {(vt_mpe)*100} %
        Absolute Error: 
            Max error           {vt_max_error*a} cm^3 
            Most Probable Error {vt_mpe*a} cm^3
            """)

if __name__ == "__main__":
    main()
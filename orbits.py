from vpython import *
#Web VPython 3.2

# simple Earth-Sun-Moon simulation B. Philhour 8/16/15 - 2/22/18
# Adapted to export data and have inputs in the UI. Alex Berman 4/11/2024

# constants - use these to change the scale and initial positions of everything
# the basic issue here is that realistic size scales would be impossible to see, so we choose unrealistic values for ease of visualization

realSunRadius = 696000000        # the actual radius of the Sun in meters - amazing, huh?
sunRadius = 10 * realSunRadius   # the size for our solar system
earthRadius = sunRadius * 0.25    # note: real value would be sunRadius * 0.01, a good choice for sim is * 0.25
marsRadius = sunRadius * 0.5
astronomicalUnit = 212.7 * realSunRadius     # the distance from Sun to Earth - the Sun is about 100 Sun diameters away      
gravity = 6.6e-11   # sets the strength of the gravitational constant to 6.6x10-11 Newton x meters squared per kilograms squared

print("IMPORTANT: READ INSTRUCTIONS BELOW")
print("Press the control key and drag your mouse to orbit around the scene. Input different variables to see how the orbits change. If you are changing a variable you MUST PRESS ENTER to save it to your simulation. If you make the sun or planets too big, the animation will go black, but the data will still be correct.")

# create the Sun object
sun = sphere( radius = sunRadius, opacity = 0.7, emissive = True, color=color.yellow) 
sun.mass = 2e30   # mass of the Sun in kilograms is 2,000,000,000,000,000,000,000,000,000,000 kg
sun.pos = vec(0,0,0)
sun.vel = vec(0,0,0)

mars = sphere( radius = marsRadius, opacity = 0, emissive = True, texture = "https://upload.wikimedia.org/wikipedia/commons/0/02/OSIRIS_Mars_true_color.jpg")
mars.mass = 6.39e23   # mass of the Sun in kilograms is 2,000,000,000,000,000,000,000,000,000,000 kg
mars.pos = vec(1.5 * astronomicalUnit,0,0)
mars.vel = vec(0,0,-24000)
#attach_trail(mars, radius = mars.radius/2, color = color.red, retain = 1000)


# place a few sources of light at the same position as the Sun to illuminate the Earth and Moon objects
sunlight = local_light( pos = vec(0,0,0), color=color.white )
more_sunlight = local_light( pos = vec(0,0,0), color=color.white )  # I found adding two lights was about right

# create the Earth object
earth = sphere ( radius = earthRadius, color=color.blue, flipx = False , shininess = 0.9, make_trail=True, trail_radius = earthRadius/2, color=color.cyan, retain=1000)
earth.mass = 6e24   # mass of Earth in kilograms
earth.pos = vec(astronomicalUnit, 0, 0)
earth.vel = vec(0,0,-30000)   # the Earth is moving around 30000 m/s
#attach_trail(earth, radius = earth.radius/2, color = color.cyan, retain = 1000)



scene.camera.follow(sun)   # have the camera default to centering on the sun
following = sun 

exportsButton = button(text = "Export Data", bind = exports)


# make CSV Ms, Me, Posx, Posy, Fx, Fy, Vx, Vy (on Earth)
data = [["Sun Mass", "Earth Mass", "X Position of Earth", "Y Position of Earth", "X Position of Sun", "Y Position of Sun", "X Force on Earth", "Y Force on Earth", "X Velocity of Earth", "Y velocity of Earth", "X Velocity of Sun", "Y velocity of Sun"]]

def exports():
    csv_str = ''
    for row in data:
        for i in range(len(row)):
            cell = row[i]
            if i != 0:
                csv_str += ","
            filtered_string = str(cell).replace(",", ";")
            csv_str += filtered_string
        csv_str += '\n'
        
    # Create a link element
    link = document.createElement('a')
    # Set the href attribute to the CSV data
    link.href = 'data:text/csv;charset=utf-8,' + encodeURIComponent(csv_str)
    # Set the download attribute to specify the filename
    link.download = 'data.csv'
    # Append the link to the document body
    document.body.appendChild(link)
    # Simulate a click on the link to trigger the download
    link.click()
    # Remove the link from the document body
    document.body.removeChild(link)
    print("exported")

run = True
    

# Create a text input box
earthIn1 = winput(prompt="Earth velocity:", bind=earthvel, text=-30000)
earthIn2 = winput(prompt="Earth mass:", bind=earthmass, text=6e24)
sunIn1 = winput(prompt="Sun mass:", bind=sunmass, text=2e30)


def earthvel(evt):
    earth.vel = vec(0,0,evt.number)
def earthmass(evt):
#    earth.radius = earth.radius*((((evt.number/earth.mass)-1)/20)+1)
    earth.mass = evt.number
def marsvel(evt):
    mars.vel = vec(0,0,evt.number)
def marsmass(evt):
#    mars.radius = mars.radius*((((evt.number/mars.mass)-1)/20)+1)
    mars.mass = evt.number
def sunmass(evt):
#    sun.radius = sun.radius*((((evt.number/sun.mass)-1)/20)+1)
    sun.mass = evt.number

    
startButton = button(text = "Start", bind = restart)
    

def restart():
    pauseButton = button(text = "Pause", bind = pause)
    
    def pause():
        global run
        run = not run
        if run:
            pauseButton.text = "Pause"
            unpause()
        else:
            pauseButton.text = "Resume"
    
    earthIn1.delete()
    earthIn2.delete()
    sunIn1.delete()
    startButton.delete()
    
    earth.clear_trail()
    mars.clear_trail()
    realSunRadius = 696000000        # the actual radius of the Sun in meters - amazing, huh?
    sunRadius = 10 * realSunRadius   # the size for our solar system
    earthRadius = sunRadius * 0.25    # note: real value would be sunRadius * 0.01, a good choice for sim is * 0.25
    marsRadius = sunRadius * 0.5
    astronomicalUnit = 212.7 * realSunRadius     # the distance from Sun to Earth - the Sun is about 100 Sun diameters away      
    gravity = 6.6e-11   # sets the strength of the gravitational constant to 6.6x10-11 Newton x meters squared per kilograms squared
    
    sun.pos = vec(0,0,0)
    sun.vel = vec(0,0,0)
    
    mars.pos = vec(1.5 * astronomicalUnit,0,0)
    #attach_trail(mars, radius = mars.radius/2, color = color.red, retain = 1000)
    
    
    # place a few sources of light at the same position as the Sun to illuminate the Earth and Moon objects
    sunlight = local_light( pos = vec(0,0,0), color=color.white )
    more_sunlight = local_light( pos = vec(0,0,0), color=color.white )  # I found adding two lights was about right
    
    # create the Earth object
    earth.pos = vec(astronomicalUnit, 0, 0)
    #attach_trail(earth, radius = earth.radius/2, color = color.cyan, retain = 1000)
        
    
    counter = 0
    # below is the main loop of the program - everything above is "setup" and now we are in the main "loop" where all the action occurs

    dt = 10000
    programSpeed = 0.02
    counter = 0
    
    f_grav = gravity * sun.mass * earth.mass * (sun.pos - earth.pos).norm() / (sun.pos - earth.pos).mag2
    
    data.append([sun.mass, earth.mass, earth.pos.x, earth.pos.z, sun.pos.x, sun.pos.z, f_grav.x, f_grav.z, earth.vel.x, earth.vel.z, sun.vel.x, sun.vel.z])
    global run
    
    
    while (run):   # this will make it loop forever
        rate(100)   # this limits the animation rate so that it won't depend on computer/browser processor speed
        counter += 1
        # calculate the force of gravity on each object
        f_grav = gravity * sun.mass * earth.mass * (sun.pos - earth.pos).norm() / (sun.pos - earth.pos).mag2
        f_grav1 = gravity * mars.mass * sun.mass * (sun.pos - mars.pos).norm()/ (sun.pos - mars.pos).mag2
        earth.vel = earth.vel + (f_grav/earth.mass) * dt
        sun.vel = sun.vel - (f_grav/sun.mass) * dt
        mars.vel = mars.vel + (f_grav1/mars.mass) * dt
        # update the position of the Earth and Moon by using simple circle trigonometry
        earth.pos = earth.pos + earth.vel * dt 
        sun.pos = sun.pos + sun.vel * dt
        mars.pos = mars.pos + mars.vel * dt
        
        if counter%100 == 0:
          print("Earth velocity:", earth.vel, "Sun velocity:", sun.vel)
          print("Earth position:", earth.pos, "Sun position:", sun.pos)
          print("Force on Earth:", f_grav)
          print()
          
          data.append([sun.mass, earth.mass, earth.pos.x, earth.pos.z, sun.pos.x, sun.pos.z, f_grav.x, f_grav.z, earth.vel.x, earth.vel.z, sun.vel.x, sun.vel.z])
          
        # cause the Earth and Moon to rotate on their own axis - to flip one of them, make the middle entry in the axis vector (-1) 
        earth.rotate (angle = radians(programSpeed * 360), axis = vec(0, 1, 0))   # rotate the earth 360 times per year
        sun.rotate (angle = radians(programSpeed * 16), axis = vec(0, 1, 0))     # rotate the Sun with a period of about 22 days
    
def unpause():
    dt = 10000
    programSpeed = 0.02
    counter = 0
    while (run):   # this will make it loop forever
        rate(100)   # this limits the animation rate so that it won't depend on computer/browser processor speed
        counter += 1
        # calculate the force of gravity on each object
        f_grav = gravity * sun.mass * earth.mass * (sun.pos - earth.pos).norm() / (sun.pos - earth.pos).mag2
        f_grav1 = gravity * mars.mass * sun.mass * (sun.pos - mars.pos).norm()/ (sun.pos - mars.pos).mag2
        earth.vel = earth.vel + (f_grav/earth.mass) * dt
        sun.vel = sun.vel - (f_grav/sun.mass) * dt
        mars.vel = mars.vel + (f_grav1/mars.mass) * dt
        # update the position of the Earth and Moon by using simple circle trigonometry
        earth.pos = earth.pos + earth.vel * dt 
        sun.pos = sun.pos + sun.vel * dt
        mars.pos = mars.pos + mars.vel * dt
        
        if counter%100 == 0:
          print("Earth velocity:", earth.vel, "Sun velocity:", sun.vel)
          print("Earth position:", earth.pos, "Sun position:", sun.pos)
          print("Force on Earth:", f_grav)
          print()
          
          data.append([sun.mass, earth.mass, earth.pos.x, earth.pos.z, sun.pos.x, sun.pos.z, f_grav.x, f_grav.z, earth.vel.x, earth.vel.z, sun.vel.x, sun.vel.z])
          
        # cause the Earth and Moon to rotate on their own axis - to flip one of them, make the middle entry in the axis vector (-1) 
        earth.rotate (angle = radians(programSpeed * 360), axis = vec(0, 1, 0))   # rotate the earth 360 times per year
        sun.rotate (angle = radians(programSpeed * 16), axis = vec(0, 1, 0))     # rotate the Sun with a period of about 22 days

        
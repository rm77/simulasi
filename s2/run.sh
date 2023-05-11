docker run --rm \
   -ti -e DISPLAY=$DISPLAY \
   -v /tmp/.X11-unix:/tmp/.X11-unix \
   mmodenesi/omnetpy bash

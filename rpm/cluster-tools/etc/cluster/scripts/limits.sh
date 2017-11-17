#!/bin/bash
# Set the limits for MPI on the nodes
cat << EOF > /etc/security/limits.d/memlock.conf
*               hard     memlock         unlimited
*               soft     memlock         unlimited
*               hard     stack         unlimited
*               soft     stack         unlimited
EOF


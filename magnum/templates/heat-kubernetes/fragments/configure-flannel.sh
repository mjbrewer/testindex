#!/bin/sh

. /etc/sysconfig/heat-params
. /etc/sysconfig/flanneld

FLANNEL_JSON=/etc/sysconfig/flannel-network.json

if [ "$FLANNEL_USE_VXLAN" == "true" ]; then
	use_vxlan=1
fi

# Generate a flannel configuration that we will
# store into etcd using curl.
cat > $FLANNEL_JSON <<EOF
{
  "Network": "$FLANNEL_NETWORK_CIDR",
  "Subnetlen": $FLANNEL_NETWORK_SUBNETLEN
EOF

if [ "$use_vxlan" = 1 ]; then
cat >> $FLANNEL_JSON <<EOF
  ,
  "Backend": {
    "Type": "vxlan"
  }
EOF
fi

cat >> $FLANNEL_JSON <<EOF
}
EOF

# wait for etcd to become active (we will need it to push the flanneld config)
while ! curl -sf -o /dev/null $FLANNEL_ETCD/v2/keys/; do
  echo "waiting for etcd"
  sleep 1
done

# put the flannel config in etcd
echo "creating flanneld config in etcd"
curl -sf -L $FLANNEL_ETCD/v2/keys/coreos.com/network/config \
  -X PUT \
  --data-urlencode value@/etc/sysconfig/flannel-network.json


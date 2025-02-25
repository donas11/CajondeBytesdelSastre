 [inlets ](https://inlets.dev/)
 [doc inlets](https://docs.inlets.dev/)
 [inlets-operator](https://github.com/inlets/inlets-operator)

Whether using push or pull-based administration, realistic testing is important. You should consider the following:

Are there any requirements around latency?
How much data will be transferred and how often?
What happens if and when a link is unavailable for a period of time?




By the end of this chapter, we will cover the following:

## Partial connectivity and bandwidth

For devices at the edge, there may be no Internet or cellular connection available at all, which means that data can only be collected by visits from an engineer to a site. An example of this would be a data-logger by a riverside, there to detect flow and water levels.

Where devices have cellular modems that access a 3G network, bandwidth is charged per MB, so being always connected could be expensive, especially at scale. In this instance, the device will need to call home or connect to the network on an interval to save on costs.

Cloud software doesn’t tend to be developed to cope with unreliable or partially available network access, but a prime example would be a mobile phone running an operating system like Android. During a flight, or an underground train journey, you will have no access to the network, but when you are able to connect again, the device can re-synchronize.



# Access to storage

Why would you want storage for edge devices?

For the system drive which runs and operating system and K3s
For any data samples or data which is logged
To store container images that are run inside the K3s cluster
There are concerns when it comes to storage at the edge:

Latency - is it fast enough?
Capacity - will it run out?
Reliability - is it going to tolerate a failure?

Mean time to recover from a failure

The Raspberry Pi’s SD card for instance has very high latency storage with low capacity when compared to an NVMe (Non-Volatile Memory Express) drive attached over USB.

The Raspberry Pi can also be net-booted over a NAS, which increases reliability and capacity, but the latency also increases compared to a local USB drive.

# Recap on Edge Compute

So, whilst Kubernetes is not the only option available, it does have the advantage of offering a homogenous platform if you adopt it at the edge and in your datacenter. K3s makes it even easier to deploy Kubernetes at the edge, and the two are interoperable. Technologies like GitOps and Rancher’s Fleet project can make it easier to manage large numbers of devices or clusters.
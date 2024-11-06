---
title: Openshift
created: '2024-11-02T00:46:13.862Z'
modified: '2024-11-02T00:55:28.429Z'
---

# Openshift

1. Log in to OpenShift cluster:

```oc login <cluster-url>```



2. View your current context:

```oc config current-context```



3. Create a new project:

```oc new-project <project-name>```



4. Switch to a different project:

```oc project <project-name>```



5. List all projects in the cluster:

```oc get projects```



6. List all pods in the current project:

```oc get pods```



7. Describe a specific pod:

```oc describe pod <pod-name>```



8. List all services in the current project:

```oc get services```



9. Describe a specific service:

```oc describe service <service-name>```



10. List all deployments in the current project:

```oc get deployments```



11. Describe a specific deployment:

```oc describe deployment <deployment-name>```



12. Scale a deployment:

```oc scale --replicas=<desired-replicas> deployment/<deployment-name>```



13. Create a new application from a Git repository:

```oc new-app https://github.com/your/repo.git```



14. Expose a service:

```oc expose service <service-name>```



15. Create a route for a service:

```oc create route edge --service=<service-name>```



16. List all routes in the current project:

```oc get routes```



17. List all persistent volume claims in the current project:

```oc get pvc```



18. Describe a specific persistent volume claim:

```oc describe pvc <pvc-name>```



19. Create a new secret:

```oc create secret generic <secret-name> --from-literal=<key>=<value>```



20. List all secrets in the current project:

```oc get secrets```



21. Describe a specific secret:

```oc describe secret <secret-name>```



22. List all ConfigMaps in the current project:

```oc get configmaps```



23. Describe a specific ConfigMap:

```oc describe configmap <configmap-name>```



24. List all persistent volumes in the cluster:

```oc get pv```



25. Describe a specific persistent volume:

```oc describe pv <pv-name>```



26. List all roles in the current project:

```oc get roles```



27. Describe a specific role:

```oc describe role <role-name>```



28. List all role bindings in the current project:

```oc get rolebindings```



29. Describe a specific role binding:

```oc describe rolebinding <rolebinding-name>```



30. List all cluster roles:

```oc get clusterroles```



31. Describe a specific cluster role:

```oc describe clusterrole <clusterrole-name>```



32. List all cluster role bindings:

```oc get clusterrolebindings```



33. Describe a specific cluster role binding:

```oc describe clusterrolebinding <clusterrolebinding-name>```



34. List all image streams in the current project:

```oc get is```



35. Describe a specific image stream:

```oc describe is <imagestream-name>```



36. List all build configurations in the current project:

```oc get bc```



37. Describe a specific build configuration:

```oc describe bc <buildconfig-name>```



38. Start a new build from a build configuration:

```oc start-build <buildconfig-name>```



39. List all builds in the current project:

```oc get builds```



40. Describe a specific build:

```oc describe build <build-name>```



41. List all deployment configs in the current project:

```oc get dc```



42. Describe a specific deployment config:

```oc describe dc <deploymentconfig-name>```



43. Rollout a new deployment configuration:

```oc rollout latest <deploymentconfig-name>```



44. List all services accounts in the current project:

```oc get serviceaccounts```



45. Describe a specific service account:

```oc describe serviceaccount <serviceaccount-name>```



46. List all routes in the current project:

```oc get routes```



47. Describe a specific route:

```oc describe route <route-name>```



48. List all pods in all projects:

```oc get pods --all-namespaces```



49. List all services in all projects:

```oc get services --all-namespaces```



50. List all nodes in the cluster:

```oc get nodes```



51. Describe a specific node:

```oc describe node <node-name>```



52. List all namespaces in the cluster:

```oc get namespaces```



53. Describe a specific namespace:

```oc describe namespace <namespace-name>```



54. List all custom resource definitions (CRDs) in the cluster:

```oc get crd```



55. Describe a specific custom resource definition (CRD):

```oc describe crd <crd-name>```



56. List all custom resources (CRs) in the current project:

```oc get cr <cr-name>```



57. Describe a specific custom resource (CR):

```oc describe cr <cr-name>```



58. List all roles in all projects:

```oc get roles --all-namespaces```



59. List all role bindings in all projects:

```oc get rolebindings --all-namespaces```



60. List all cluster roles in all projects:

```oc get clusterroles --all-namespaces```



61. List all cluster role bindings in all projects:

```oc get clusterrolebindings --all-namespaces```



62. List all security context constraints (SCCs) in the cluster:

```oc get scc```



63. Describe a specific security context constraint (SCC):

```oc describe scc <scc-name>```



64. List all limit ranges in the current project:

```oc get limitranges```



65. Describe a specific limit range:

```oc describe limitrange <limitrange-name>```



66. List all network policies in the current project:

```oc get networkpolicies```



67. Describe a specific network policy:

```oc describe networkpolicy <networkpolicy-name>```



68. List all resource quotas in the current project:

```oc get quota```



69. Describe a specific resource quota:

```oc describe quota <quota-name>```



70. List all service catalog brokers:

```oc get brokers```



71. Describe a specific service catalog broker:

```oc describe broker <broker-name>```



72. List all service catalog service classes:

```oc get serviceclasses```



73. Describe a specific service catalog service class:

```oc describe serviceclass <serviceclass-name>```



74. List all service catalog service instances:

```oc get serviceinstances```



75. Describe a specific service catalog service instance:

```oc describe serviceinstance <serviceinstance-name>```



76. List all service catalog service bindings:

```oc get servicebindings```



77. Describe a specific service catalog service binding:

```oc describe servicebinding <servicebinding-name>```



78. List all storage classes in the cluster:

```oc get sc```



79. Describe a specific storage class:

```oc describe sc <storageclass-name>```



80. List all image streams in all projects:

```oc get is --all-namespaces```



81. List all build configurations in all projects:

```oc get bc --all-namespaces```



82. List all deployment configs in all projects:

```oc get dc --all-namespaces```



83. List all secrets in all projects:

```oc get secrets --all-namespaces```



84. List all ConfigMaps in all projects:

```oc get configmaps --all-namespaces```



85. List all persistent volume claims in all projects:

```oc get pvc --all-namespaces```



86. List all custom resources (CRs) in all projects:

```oc get cr --all-namespaces```



87. List all roles in all projects:

```oc get roles --all-namespaces```



88. List all role bindings in all projects:

```oc get rolebindings --all-namespaces```



89. List all cluster roles in all projects:

```oc get clusterroles --all-namespaces```



90. List all cluster role bindings in all projects:

```oc get clusterrolebindings --all-namespaces```



91. List all service catalog brokers in all projects:

```oc get brokers --all-namespaces```



92. List all service catalog service classes in all projects:

```oc get serviceclasses --all-namespaces```



93. List all service catalog service instances in all projects:

```oc get serviceinstances --all-namespaces```



94. List all service catalog service bindings in all projects:

```oc get servicebindings --all-namespaces```



95. List all roles in a specific project:

```oc get roles -n <project-name>```



96. List all role bindings in a specific project:

```oc get rolebindings -n <project-name>```



97. List all cluster roles in a specific project:

```oc get clusterroles -n <project-name>```



98. List all cluster role bindings in a specific project:

```oc get clusterrolebindings -n <project-name>```



99. List all security context constraints (SCCs) in a specific project:

```oc get scc -n <project-name>```



100. List all limit ranges in a specific project:

```oc get limitranges -n <project-name>```


<template>
  <q-page class="flex column flex-center">
    <div class="column q-gutter-md">
      <q-input outlined dense v-model="username" placeholder="Name" />
      <q-btn label="Click Me!" @click="onSubmit" />
    </div>
    <div class="max-width: 400px">{{ grpcResponse }}</div>
  </q-page>
</template>

<script>
import { defineComponent, ref } from "vue";
import { HelloReq } from "../api/simple_grpc_pb.js";
import { SimpleGrpcClient } from "../api/simple_grpc_grpc_web_pb.js";

export default defineComponent({
  name: "IndexPage",

  setup() {
    const client = new SimpleGrpcClient("http://localhost:5000", null, null);

    const username = ref("");

    const grpcResponse = ref("");

    const onSubmit = () => {
      let req = new HelloReq();

      req.setName(username.value);

      client.sayHello(req, {}, (err, res) => {
        if (err) {
          console.log(err);
          grpcResponse.value = JSON.stringify(err);
          return;
        }
        // console.log("Response:", res);
        grpcResponse.value = JSON.stringify(res.toObject());
      });
    };

    return {
      username,
      grpcResponse,
      onSubmit,
    };
  },
});
</script>

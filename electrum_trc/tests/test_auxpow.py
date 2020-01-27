from electrum_trc import auxpow, blockchain, constants
from electrum_trc.util import bfh, bh2u

from . import SequentialTestCase
from . import TestCaseForTestnet
from . import FAST_TESTS

header_833004 = '04013200b616af1f0cfc620cdd9742e5e957db32f12cfb46a1f8fcc14fdd289c4984b688a258d7d295b1672788113bc6522b8e09730d109f567d1b2943f4186aba4b9e27031ee557ad552e1a0000000001000000010000000000000000000000000000000000000000000000000000000000000000ffffffff31030c94062cfabe6d6d995807770acf351e0cfebcce6916cd79f9818a4e331b8c7832f524f32f3c92722000000000000000ffffffff59071f0000000000001976a914415b1b88521a33e429bff034f2a2fd2fd7fc82ad88ac4c1f0000000000001976a914bf01de4a5128e4017e4ef2d14d4ef01e386faa3088ac741f0000000000001976a914b9ba1682116634e56b4e091ed340a852b454315a88aca43c0000000000001976a914d5c39ef27b3c7a25c1d25a9b2a3fabb02e2dba8d88ac378d0000000000001976a914e02fcb731ba8f15bbe69c77ab9a5df675770b97488acafa40000000000001976a9140bb84a507ab8935a48de8784f324e37baac6011d88acebc00000000000001976a9141ed3470c917bb7e377473be131c5f8f1d33fa12588ac3c270100000000001976a914d2d038a2d76b67b4cec35f534fea3b7c76db06e788ac31710100000000001976a914f446010a1324f2998385815121f3422c0fe0ac0c88acedaf0100000000001976a914025184877d19593ac712d05fec5a5a79c339618e88ac6cea0100000000001976a914fb5c2fff658536c4a66023294489ff641f50870688ac05210200000000001976a914390f47d1be034e5b96695f0902cde725c23747d288acbd370200000000001976a914801203fc3c8cb57c036a92769cb0eb63d6cd789888ac93550200000000001976a914d1fd4a8f107532c4d34120f511f6f75bfc923a4188ac7f630200000000001976a914efe4a88a5e981cd0ffbb2172e5d53d04a4f8858288ac83d20200000000001976a914f54e8b762ff17c06a71f2a523dbe51238d523cfd88ac66e00200000000001976a914436846875331bd459413c52045508720744ac41488ac35480300000000001976a9142071be3ebd5e6d7323fc3f9aaa4ac8a38685da2288acbe610300000000001976a91409d03379c0c27a011b23e8d186de2e4c1be3689b88acc3770300000000001976a914465bb9d40011ea0ec97776f8ce1a2e4590c7b86388ac5faf0300000000001976a9144dfc0b493a05b3ce1cc2a28ed5380ce1d3e76fab88acddb40300000000001976a9148d773b51089a9621052851c7503a57525f772ee088ac88ba0300000000001976a9142712932c661c78957fdf611652f1b4b75e52934088ac37580500000000001976a9147c6b2f1bf7c45d5516f707ee95ebc1493825f90788ac0cd70500000000001976a9143431da1db1dd42402f806ecfb88d66eede20a13188ac7be40500000000001976a914e85bf07f267cabcd61f05083c84dcfbebfa0ee5e88ac12460600000000001976a9147d4604279d053aed391dc76ee04103b0f9ca458188ac3c530600000000001976a9141e8dc5961ddfca54a2ff90a2759b0492eb4c1d7b88ac667e0600000000001976a914d6e65bc21a93c2a15d5bfb0e8ea059f5f8bab24188acc6fd0600000000001976a914d037446d62a80a3cb84ebed207e8268eb2f43e9088ac890e0700000000001976a9140809d9e2b5011d4719efed4be816d072965493de88aca7250700000000001976a9145e100fa1f9816e4977fb0f584dcb5699b83496b188acb0520700000000001976a914e1c0dcf3775c0f9d5131e781fb11a7b0f858195488ac34590900000000001976a9148c84a5163bac3849d2e41308278190d955ad938388ac2d5a0900000000001976a9148e652be4a3475cbeda073956e87783bfaa32053d88ac06aa0b00000000001976a91495fedc518c216bc0e8ccfabb1be676fc744c76fb88aca8d00b00000000001976a91417881c8cf9654f50ac205ed8c9dc3a4970d9c62188ac4c180c00000000001976a91478e8c7c0ba120dfc15f2e8405464c2032cbf7e2d88ac36430c00000000001976a914ee86bc8f30c9a5f7a8302e9140e87cd765b796ff88ace0520c00000000001976a914530ee478a9bd260e30f43ef6bf01229c55b5623288acdec20d00000000001976a914b005ef7765e2e905a44496b079d83eab8f370ae788ace1300e00000000001976a91459516545dc8fb03fff98b9944c6ea375f7b88a8888ac2a770e00000000001976a91412588bb0c8bcb42f236ab368ebf09769c297481988acd0a80e00000000001976a914140f0e13a9517eeb08f1af08fdd12ec619160f6b88acf6d20e00000000001976a91495213765b708a57e214c15520ec1fbe2cba6815488ac8d7d1100000000001976a91427b4668a922eecb79411cc168475ef029b820db188ac72021200000000001976a914ac2cab5240e0f1c4fb62d93e0f34c27d50f1a9d188ac01fb1200000000001976a914ecc2daa2ed9fb7933854c8b80a724cc51e71108288ac94431300000000001976a914274f5f0cfe4bb42fda59156ee1e1bc1ee56ee7bc88acabd21500000000001976a914b2b2ace0ef8a129cf1410ca38de376e57165ff5788acf7271600000000001976a9146d45bfe5c5e5e27fea1215882fde091695339b5088ac10631600000000001976a9149679d2f3b7f2ba15ed74adc53a6fb1ba0a5dfcb688ac31ac1700000000001976a914356469ddbf0ec76d74604f65553d7b26dee619ee88acaa631a00000000001976a9140805568a51b1892db5b4d427b8782f5394607eb688ac06a61b00000000001976a9141aa1661ec979b90c5f5d330fb6eca5003c35e18e88ac4cf62600000000001976a9141ad7d4a4f278c5ffac4e64c4ad942f512a8c6c5388aca2d22900000000001976a91494fcb90fea313fa88221cbd9213967fd35fc468988accc832a00000000001976a914301db9645f73c61282045b701fd7a3bc6611a46188acfe402c00000000001976a91491326ea24c845cd78eb460cf4c91d6111736237488ac4a852d00000000001976a9142e66df7163166ac7339c9a4306ce7a1a3b9d61c788ac79793000000000001976a91406398f2c64fbe6388f258caf359f45377087156d88ac25f33000000000001976a9144c257731b9bae64dfb14203e784cc6bd4f900a4288ac00ab3900000000001976a9141246c8f9ced7d39799d4854b2961e263194bdb6888acffb13a00000000001976a914da809961b865794f43e04ec11d01ff2c77d68d5a88ac4e274500000000001976a914b0f6bbcaaa3979c487a2c601b804b70a4309c48988ac21764b00000000001976a914e3aaa9933e859cab6d2af23222d022973fea141d88ac66215100000000001976a9149b3993108edb852b85060b40e2857bd8a90e5d6388ac47f55700000000001976a914121f043be3762630d3fda1c6b15be1df111bf13c88acb46c7500000000001976a914b764dd0a8cc279f9715670c2d741e4bb95b58eb388ac2ac18600000000001976a914cedabd406303a5a01cdae0375f50c447f2ad5fd188ac0a8f8e00000000001976a914bd50057b57b5b44c56da410233b3d424b61ac8af88ac673d9100000000001976a9147a894199c6a485cbe4bd0508b1a21304e32cc25088acbfd79800000000001976a9145da8d4900073aa2c6b77b67eaedcdc6f3146b38c88acdd469b00000000001976a914a7b2609a0e4f3c1a003483eae14ab39c2f83143388acb1269d00000000001976a914a6409365cbbdb32b6d5245d77a44d20bb1b88bdb88acc517cb00000000001976a914fb212bd0a013c906c556e9b764916677edcb29e188aca027cb00000000001976a9148bf60f5ce9e6096656e2c648a67ec824b8460ba488acea00e700000000001976a914b535e79403688a1052567c8645c92aebe6421baa88ac7b8ef800000000001976a914049fa7271177a8573d15ebcf20c5f74b9a8b780388ac17fc7f01000000001976a914ebccd3780bdb7d66ff1f8bbabc83d8672284fe8c88ace616b802000000001976a914dcf2a7cf5cd8ef588ca03d43c8a82002e678d12e88ac3dcc4803000000001976a914f12ccbe526747d913e6d80d6ee58c2e5b6e09d5c88acad789c03000000001976a9140f69c105fe00d56f0a31d835370606bb7d7b7a0788ac0c14b805000000001976a914ce963869027732b277062f3fbe1d9c974bb679ff88acc274100a000000001976a9149c3db6bc1c0f437ddddac78eee771d36e00fcd1488ac3b39d30b000000001976a9143e7b8e9f136c13baf0b261bf67a8c0410a51a2f988ac7d3ec319000000001976a914ae6a2f5b8268c54a9d1ac5d8a44551443240f3c388ac184e0c0000000000434104ffd03de44a6e11b9917f3a29f9443283d9871c9d743ef30d5eddcd37094b64d1b3d8090496b53256786bf5c82932ec23c3b74d9f05a6f95a8b5529352656664bac00000000000000002a6a28c159017a38b4e35be7c884375c4b41b5e1624c9e8cd56a783c393f3f9537a63c0000000062d5010000000000515759d512d3fb2691cbe207186477834778171a82fb05b31a200000000000000bfc6aec8a6e66369deaad4bd83ea123228f4d9bf3401026eda4307ac9b2346792ad3e772d2e35f8d5658035cac1e907d01c6557e9cc0e2bba5fed3fa2b48228f24508d327b76b7b1e5aa59e371adfe97af46d2558187d12494014c1be0a5725e4f07748c13be80f6679acbdc93c61b4e3c1852d5cc7af682e0caae6b4bdee78d1838d4484b932d63f5349002fe2b9c693ab856b90311b759d312bb439eaa0fc709c8768db819280d03f44894dcf10142e76f9dc9390960d835c3a336169ad83aeaf737e17fec27e1fb17974190f8a535e782e41a3bf301087af517864c99e51f6256755ddc564f291e1f057e2f59842f72746b5a43d64c50402128879d19fdb6189cbb02cb5728b22c9969a99f199318184354f81d56192e077447746d5ccce0fccb79aadceea33ba9cc118b101c6c1c0ce17f70c32162a15b3b8316c97ac2aacb597a25871c04b2cf80471ec4132fc54d6dd8bc74615341845803790583a677f000000000500000000000000000000000000000000000000000000000000000000000000002a39f63a70dbbf56ce418fde61c3229d88d1ee3ee186ed09612586fb99bbbab2550dcac0863cbcab19e2032a3d4189c5a96b0e6d9787c91f27b27c87054cddc8d2e5df2bdf80e48b3f370bf773a4623f883838ece03e29f8d0bc7d27ae22c2b623ba8cf470f7448d12c84e1266697fc1e07abf5862088d1cb458c652bfc505f308000000000000202919d3aee24f27786d811063c8598100c68833751e0ac4020000000000000000eebf64723e0c55d9e6cad2a49ba66ec4a1479b1e0231030f1f9de239b3b2ee46011ee5575ede0418ce0444c0'

header_833204 = '04013200e1c9f9b262227a051a150f567fbb01da5b7820ba03a651338fedb23a8f89a34f358f16475da7a66e8619b81afeb96d34e15752c85b440333c41f85d57759db5eec64e55747c3011a0000000001000000010000000000000000000000000000000000000000000000000000000000000000ffffffff51038dd706062f503253482f04ee64e5570881002846dd0c01007777772e7a706f6f6c2e6361fabe6d6df1f8037fc736cf65c651ca9b83d747fcc869a0184904b6eea3343e5c616249991000000000000000000000000180b2e60e000000001976a914f7723b20cc8025afd602aaafa8cdd1b272b2a48588ac00000000000000000000014e523d223d05db4246a0aea41677a7f15ee057f48a97b13da80283be59f4d89de176953e83197a189112d302e416df23e3d9efc17fd5c9a9e30eb8a0e86f25899941c3a084db6a03e17ede46cf0cce5644409b6157e19caaaa9400000000040000000000000000000000000000000000000000000000000000000000000000842a46ec60b691b8226bce2544bf6949d166d2ad6e61d9fa896804a19ecd52d3f3c0bf4f46fcaca9b8bf704d2701bf465c2042a52623ab41a15bc8e62d5432446966a1b584eb77638529438229660ab6f9cdfd3c7ed989f413cebd7eba2654a5080000000202000089b89a5476216df0d6da96e2e553c404946635083a4434a5f6721f9451074f3aa7402782938b720660ac9697c574a1df770465b903a3ca05a73468e12773fb58ef64e55777c6021a2fc598a8'
prev_hash_833204 = '4fa3898f3ab2ed8f3351a603ba20785bda01bb7f560f151a057a2262b2f9c9e1'
target_833204 = blockchain.Blockchain.bits_to_target(436323143)

header_850964 = '04013200bb9d496ee95b1e12193217bda1aa8f1899408c3a28d346075ea6cedcb9426cb56ecf38e55b43be105591d301b5a435583af4bfe86423794d4ca1ba0f5b12804f78c1075866eb011a0000000001000000010000000000000000000000000000000000000000000000000000000000000000ffffffff310354a3062cfabe6d6d675f5bade2a0d3161409d10a740c783bd8c820871e637de51eb4f28ccdae478a2000000000000000ffffffff8f0b240000000000001976a914ed3104267d771aeaf7fe9a7fd5dc56f2dc18ad8f88ac77240000000000001976a914475e690a516414a88d0ac15abbc7fd0538acd16988ac0d250000000000001976a9141ed3470c917bb7e377473be131c5f8f1d33fa12588aca35c0000000000001976a914d0021524edd71477d0a252e78afc320668908fda88ac47770000000000001976a914d2d038a2d76b67b4cec35f534fea3b7c76db06e788acfbbe0000000000001976a914d1fd4a8f107532c4d34120f511f6f75bfc923a4188aca0030100000000001976a914480f1f7344411190da7092d8165fb5089801ee1e88ac580b0100000000001976a9140717ef68198e96a87c92bbd94877eafa9f4f9e2988ac33140100000000001976a9140809d9e2b5011d4719efed4be816d072965493de88ac534c0100000000001976a914298b77b28ca639b66bde0758cef1f786b6af942088acef500100000000001976a9144dfc0b493a05b3ce1cc2a28ed5380ce1d3e76fab88ac8fa00100000000001976a914465bb9d40011ea0ec97776f8ce1a2e4590c7b86388acfca80100000000001976a914022547aa4a8e4414db1b8a0f2e73d0ba7b6f0fd388ac54de0100000000001976a914801203fc3c8cb57c036a92769cb0eb63d6cd789888acefe70100000000001976a91453c0e66b36c3c5ec8f7b14c2f6fda22f0d9c630088ac03f10100000000001976a91478e8c7c0ba120dfc15f2e8405464c2032cbf7e2d88ac89f60100000000001976a914039dd67e07007552e1310aa06441147c8d63b3f888accb080200000000001976a914d06d8fa0c3d0c0102446f5dbb95572003d372f9388acca2b0200000000001976a914ecc2daa2ed9fb7933854c8b80a724cc51e71108288aca93c0200000000001976a914a4f63a9bdacb5aec25e667a1092711e5f9f3d88188ac05560200000000001976a9149729f63b8a39cf39b116f8ff1b7a4c0ce00724ca88ac025a0200000000001976a9145ad95839ba6597b51766d5c9960941c1cc2d2ded88acb56c0200000000001976a914d06f6e9ca38ceb85f1715df09e7b9b32114f240688ac76860200000000001976a914009a34e28e14838c86ca5202c57c9bd92fbff3fa88acabb80200000000001976a914d1eed5120dbec2894f77d7a4dfdda668115cf45088ac60e20200000000001976a914390f47d1be034e5b96695f0902cde725c23747d288acd2e40200000000001976a914efe4a88a5e981cd0ffbb2172e5d53d04a4f8858288ac9be80200000000001976a914fb5c2fff658536c4a66023294489ff641f50870688ac53ee0200000000001976a9141e8dc5961ddfca54a2ff90a2759b0492eb4c1d7b88ace8040300000000001976a914d06eaf04f5507440735bffbc6ee905448a6725ef88ac31350300000000001976a91494fcb90fea313fa88221cbd9213967fd35fc468988ac38590300000000001976a91457aaad14c939c6df399036639c3a68bd3ae1ec8788ac0fa90300000000001976a9149b542b30646ea02b399c7ec3ad1e5c807becd5b088ac3ce40300000000001976a914e415e0a5d6ea4d9320bb50976e663550d39ee93f88acf3fb0300000000001976a914d1edff1cf7657bb9dd76ee3254227dc4d8ed13a188ac7d120400000000001976a914f89b9f6357927e1a613df93e94d1cea064a64aef88ac522b0400000000001976a9147d4604279d053aed391dc76ee04103b0f9ca458188ac7c590400000000001976a9144206343ef54178b3679b3fd35a2b7a0da8fc61f788ac9d7a0400000000001976a9145e100fa1f9816e4977fb0f584dcb5699b83496b188ac46810400000000001976a91412588bb0c8bcb42f236ab368ebf09769c297481988accb8a0400000000001976a914eb509de7d4627c3ca355eda3b51f80e3ff7c7b8288aca0a30400000000001976a9142e66df7163166ac7339c9a4306ce7a1a3b9d61c788acd6d00400000000001976a914d0c13cfd2be612f331f27e8d0c8cda88ed30d7ee88ac1b100500000000001976a914b005ef7765e2e905a44496b079d83eab8f370ae788ace2b50500000000001976a9142071be3ebd5e6d7323fc3f9aaa4ac8a38685da2288acabc00500000000001976a9146991e05d16b8e5f4f191551ede851ba9c5270b0788acb7cd0500000000001976a91495213765b708a57e214c15520ec1fbe2cba6815488acb7e60500000000001976a91417881c8cf9654f50ac205ed8c9dc3a4970d9c62188ac5bf60500000000001976a9146d45bfe5c5e5e27fea1215882fde091695339b5088accf1d0600000000001976a9148e618a147692a5261b105f1137361acdf574101e88ac2e960600000000001976a9141edc8ddaaef01d726a185bd7c59bc1a514700e6388acebba0600000000001976a914f52e338662842c32689c4aa39753f3fc722dceda88ac03cf0600000000001976a9148e652be4a3475cbeda073956e87783bfaa32053d88ac4d5d0700000000001976a914d0c13953941678d5e413f216173530562bb5803b88acddb90700000000001976a914580fe4e39f67aedaf460de94bb9cde7be153cc6188ac7d1b0800000000001976a9145c92232239b0b2aba3408e633fe94ab1fba135c388ac13380800000000001976a914436846875331bd459413c52045508720744ac41488ac025a0800000000001976a914b9d2406492960a0c02792d60e4920acef302c9e688acd56e0800000000001976a914f2f8d04544eba7310a4705b57082c39856e4fec188ac77fe0800000000001976a91459516545dc8fb03fff98b9944c6ea375f7b88a8888ac25180900000000001976a9140b3e9bc7b3b31b6951096585943e38eb531abe5f88ac8c550900000000001976a91495fedc518c216bc0e8ccfabb1be676fc744c76fb88ac18870900000000001976a914530ee478a9bd260e30f43ef6bf01229c55b5623288aced220a00000000001976a914e85bf07f267cabcd61f05083c84dcfbebfa0ee5e88acde2b0a00000000001976a9145d6ed0076e57fc45bfaba73e32933ce55d56849e88acce340a00000000001976a914ef8ad5034c73eb3c2a9d25bb111cd9822c010a2088accb350a00000000001976a91408752f37c1ce2c5e912ccf6d7a9da5685aaeae1488acfc4a0a00000000001976a9142efb90220254e24fbe1bd11f54411a6ab6b8160988ac97be0a00000000001976a9149679d2f3b7f2ba15ed74adc53a6fb1ba0a5dfcb688acaa920c00000000001976a914a100455a54aedd3c17f9d6976a1b6cbe7c2cd95588acabaa0c00000000001976a914ac2cab5240e0f1c4fb62d93e0f34c27d50f1a9d188ac36300d00000000001976a91424b1fd2b628d7583c26fd0fa26b479e229ae876288ac51a60d00000000001976a9149c3139612cb05f08e8c90f988671999866ec6b5788acca050e00000000001976a914bea83344ab55f8ac29d9869ba6bf7c419af614c388ac40100e00000000001976a914356469ddbf0ec76d74604f65553d7b26dee619ee88acadd20e00000000001976a91495139a11c1e2ce39753ea54012cb02ed785fb9d688ac67580f00000000001976a9144c257731b9bae64dfb14203e784cc6bd4f900a4288aca5790f00000000001976a914140f0e13a9517eeb08f1af08fdd12ec619160f6b88ac8c810f00000000001976a91427b4668a922eecb79411cc168475ef029b820db188ac55381000000000001976a914ee86bc8f30c9a5f7a8302e9140e87cd765b796ff88acdea81100000000001976a9149061ca8da1569f87742034eb85ee81538c7dd9a688acccd01100000000001976a914a4ee0aa0da787fdd99063549d6e5cf24256c778c88ac3b1e1200000000001976a914e0d4e11fe309395aa44ebdd36121343948c8688388acc2901300000000001976a9141be17166b03f8d80850f2dd7a515622cb0c3334988ac95a51300000000001976a9141246c8f9ced7d39799d4854b2961e263194bdb6888ac98011400000000001976a914fba6625f61a1965e53f749efc34e813f9889447088ac3d131500000000001976a914f078182b40e405262d828a9706cf387a60c4b3a588ac1b711800000000001976a91429f2583ce64ed2f2b1a2f51cbcb5896aedd607c788ac977e1900000000001976a9140805568a51b1892db5b4d427b8782f5394607eb688ac389a1e00000000001976a9141ad7d4a4f278c5ffac4e64c4ad942f512a8c6c5388ac359a2300000000001976a91491326ea24c845cd78eb460cf4c91d6111736237488acbde72300000000001976a91406398f2c64fbe6388f258caf359f45377087156d88ac45b82400000000001976a91483663f77d63e0f795083a2c5648550163cd3d6f088acb40a2600000000001976a914301db9645f73c61282045b701fd7a3bc6611a46188ac70c72600000000001976a914e1c0dcf3775c0f9d5131e781fb11a7b0f858195488acdc4e2700000000001976a9141a0657ee9846aefe66f0e6504ee8ffb4b1ba725a88acdaa22800000000001976a914ad577cd96cb909e03cc558cc6a4af64ffc818fe388acaea32b00000000001976a9141b9b3bce69d9e019cf35992f560119bda945a82588acc3eb2e00000000001976a91404cbd817816f5d97af538b747d365fe01ac1b8e488ac621f3200000000001976a9142da5b88a34b0516881ac3fc64c8ab794b767a62988ac9c9e3200000000001976a9149928321cd79e741cb93ebd1a3be7fc0c14af140788ac22723300000000001976a914121f043be3762630d3fda1c6b15be1df111bf13c88ac02e83300000000001976a914efeab1aa0d5a17c2aff7f1f0526c164dae1f5fc088ac90363700000000001976a914301b4c70c86c533d7739bbb409c0268fe2ab320f88ac9ee23800000000001976a914dd1d437d7d7c9bd7807ad66e0789c1be4009b41088accd283900000000001976a914c2201094e8d9eef10dbbd925f608a2003105c75c88acc55c3a00000000001976a91496eb062efc2724d90073005ac96c70ec10ecc0a788acd4d04000000000001976a914b2b2ace0ef8a129cf1410ca38de376e57165ff5788acb8104600000000001976a9149c2f79f13830c59ef49124d2f94fd36d8b11aa0e88ac0ac04c00000000001976a914718e5a9aa3176051d61e5e0123a9380eedf2d9dd88ac5e705400000000001976a914a7b2609a0e4f3c1a003483eae14ab39c2f83143388ac81455500000000001976a914772ad8a1e16d16a90ee6a31b0d8e9b47423aad4088ac0cea5600000000001976a914bdb63da6deac6759e192e53e3f0d8de3770d326f88ac5dd05800000000001976a914a6409365cbbdb32b6d5245d77a44d20bb1b88bdb88ac58fc5900000000001976a914d16102d46293247c9fa75f9c78a599650cda418088accb8b5b00000000001976a914cedabd406303a5a01cdae0375f50c447f2ad5fd188ac662a6000000000001976a914bd50057b57b5b44c56da410233b3d424b61ac8af88aceaec6100000000001976a914b764dd0a8cc279f9715670c2d741e4bb95b58eb388ac5e7b6200000000001976a914c3da3cdab7b810e7d1584c121af4ba6d308eeddd88ac12c86600000000001976a9145c45b984ec511aa970ef4ebfe068cd339f72c2ab88ac5d626b00000000001976a914af227e840113cf834ce7d655e365f96527d0b1a388ac89936b00000000001976a9148bf60f5ce9e6096656e2c648a67ec824b8460ba488ac27f56e00000000001976a9145da8d4900073aa2c6b77b67eaedcdc6f3146b38c88ac3f0f8500000000001976a914ebccd3780bdb7d66ff1f8bbabc83d8672284fe8c88ac72668e00000000001976a914366026e53b0f593b4a0f95cdf6a1a22c356f1f9a88ac31b99900000000001976a914fb212bd0a013c906c556e9b764916677edcb29e188ac30c8ab00000000001976a914b535e79403688a1052567c8645c92aebe6421baa88ac420bd200000000001976a914e6021ae9d91a20bbf6328aa72b589a4284b8e89f88acd8aee500000000001976a9144957b0312d88ee32d33c0922c1f79ea4ccef166b88ac9e020001000000001976a9145e4ff6f36cb84725bd9b3aa315a3c0106bc5935c88ac23bb2001000000001976a9141a8d857e4864be9cfb222d9565ff5002beb7b53188ac08bc6001000000001976a914aa8ddd573cc4e7d0b0186b1658c4b2924e127e2788ac97b96401000000001976a914049fa7271177a8573d15ebcf20c5f74b9a8b780388acd5694e02000000001976a914f12ccbe526747d913e6d80d6ee58c2e5b6e09d5c88ac8898d302000000001976a914ce963869027732b277062f3fbe1d9c974bb679ff88ac3e218205000000001976a914a87c86a943e2b23c454cf5ac2f1ab7fc6dff99f188ac0e485a06000000001976a9149c3db6bc1c0f437ddddac78eee771d36e00fcd1488ac54086906000000001976a9143e7b8e9f136c13baf0b261bf67a8c0410a51a2f988acb6f9ee06000000001976a9140f69c105fe00d56f0a31d835370606bb7d7b7a0788acf18fdc09000000001976a914dcf2a7cf5cd8ef588ca03d43c8a82002e678d12e88acac9d990e000000001976a914ae6a2f5b8268c54a9d1ac5d8a44551443240f3c388acf857190000000000434104ffd03de44a6e11b9917f3a29f9443283d9871c9d743ef30d5eddcd37094b64d1b3d8090496b53256786bf5c82932ec23c3b74d9f05a6f95a8b5529352656664bac00000000000000002a6a28c8ccebbe248756afeff9fc22c6e996a60b9e02a46b71b41f45ee765a2ebbbbe307000000a1ee660000000000cea52acce995b8be18242cfe2ddfa4e8657a81b221a536a8740000000000000009edf3ae5713525f9a129017c4526dee420ecbe6cb1dec5f7d37c3631f9a56c95c6de8badb7636900c39aedf5d4e5acc225ab116c2e94c30a2a39632b8043772cc4eb9f7594acb0ea112d683d6fac84de2428daf1c2479332bdcb7fefa3c6c01784e8c5e3c32cebc372f40425457d7e166b04f19fec7a66a9022a4c4f840fcb643779d6d2f4b9df593c302390828cf210c6e83bbe601931aeab84b71e8fb1979089e5dd0d968d6bbc9d10f5dc64495e4f589df4db3e876fba3e4907272895de4afec14ee272792a75d5a4746d0cf4bc340edc080163a71b096d29b0509203aa62a01e94bc7097f045ce5fde595a49a232db80babc52d7c1ced1d9eeec7a61b034f2fff7d279eac98879a0366cc26bb97679f2109fc0b163cae4b3f9639c9471d7700000000050000000000000000000000000000000000000000000000000000000000000000c1cbcc4b0b240aff0bd4832b4db56841c1df317eeaba6b02185ce64f7ecb86b819e50899778ba6e34a60684b53a37780bcd12a9e1397e6cb5e0091f9f5adac58d00a96688051eae354ffbcfc8134c2874cb1e870e9163d4ec1decbd4c8234130b3afb390722a91ea0156695bb252caa49a94a4c78f56a6588f9691753d9dd33e0800000000000020d4b83d5e8e6aa350094371d005275044c7789c4830b7f90200000000000000005bf56206df79280717d5d01a8f996708e55661cd960bf21875f5069a3b53ecf71fc20758c440041846f4511a'
prev_hash_850964 = 'b56c42b9dccea65e0746d3283a8c4099188faaa1bd173219121e5be96e499dbb'
target_850964 = blockchain.Blockchain.bits_to_target(436333414)

class Test_auxpow(SequentialTestCase):

    @staticmethod
    def deserialize_with_auxpow(data_hex: str, **kwargs):
        """Deserializes a block header given as hex string
        This makes sure that the data is always deserialised as full
        block header with AuxPoW.
        The keyword-arguments expect_trailing_data and start_position can be
        set and will be passed on to deserialize_full_header."""

        # We pass a height beyond the last checkpoint, because
        # deserialize_full_header expects checkpointed headers to be truncated
        # by ElectrumX (i.e. not contain an AuxPoW).
        return blockchain.deserialize_full_header(bfh(data_hex), constants.net.max_checkpoint() + 1, **kwargs)

    @staticmethod
    def clear_coinbase_outputs(auxpow_header: dict, fix_merkle_root=True) -> None:
        """Clears the auxpow coinbase outputs
        Set the outputs of the auxpow coinbase to an empty list.  This is
        necessary when the coinbase has been modified and needs to be
        re-serialised, since present outputs are invalid due to the
        fast_tx_deserialize optimisation."""

        auxpow_header['parent_coinbase_tx']._outputs = []

        # Clear the cached raw serialization
        auxpow_header['parent_coinbase_tx'].raw = None
        auxpow_header['parent_coinbase_tx'].raw_bytes = None

        # Re-serialize.  Note that our AuxPoW library won't do this for us,
        # because it optimizes via fast_txid.
        auxpow_header['parent_coinbase_tx'].raw_bytes = bfh(auxpow_header['parent_coinbase_tx'].serialize_to_network(witness=False))

        # Correct the coinbase Merkle root.
        if fix_merkle_root:
            update_merkle_root_to_match_coinbase(auxpow_header)

    # Deserialize the AuxPoW header from Terracoin block #850,964.
    # This height was chosen because it has large, non-equal lengths of the
    # coinbase and chain Merkle branches.  It has an explicit coinbase MM
    # header.
    def test_deserialize_auxpow_header_explicit_coinbase(self):
        header = self.deserialize_with_auxpow(header_850964)
        header_auxpow = header['auxpow']

        self.assertEqual(constants.net.AUXPOW_CHAIN_ID, header_auxpow['chain_id'])

        coinbase_tx = header_auxpow['parent_coinbase_tx']
        expected_coinbase_txid = '0d1a8b9f539f19058b85dd209b1c210ec3811275aff414ce318efd5a05f23215'
        observed_coinbase_txid = auxpow.fast_txid(coinbase_tx)

        self.assertEqual(expected_coinbase_txid, observed_coinbase_txid)

        coinbase_merkle_branch = header_auxpow['coinbase_merkle_branch']
        self.assertEqual(9, len(coinbase_merkle_branch))
        self.assertEqual('5cc9569a1f63c3377d5fec1dcbe6cb0e42ee6d52c41790129a5f521357aef3ed', coinbase_merkle_branch[0])
        self.assertEqual('cc723704b83296a3a2304ce9c216b15a22cc5a4e5ddfae390c903676dbbae86d', coinbase_merkle_branch[1])
        self.assertEqual('78016c3cfafeb7dc2b3379241caf8d42e24dc8fad683d612a10ecb4a59f7b94e', coinbase_merkle_branch[2])
        self.assertEqual('43b6fc40f8c4a422906aa6c7fe194fb066e1d7575442402f37bcce323c5e8c4e', coinbase_merkle_branch[3])
        self.assertEqual('087919fbe8714bb8ea1a9301e6bb836e0c21cf28083902c393f59d4b2f6d9d77', coinbase_merkle_branch[4])
        self.assertEqual('afe45d89727290e4a3fb76e8b34ddf89f5e49544c65d0fd1c9bbd668d9d05d9e', coinbase_merkle_branch[5])
        self.assertEqual('2aa63a2009059bd296b0713a1680c0ed40c34bcfd046475a5da7922727ee14ec', coinbase_merkle_branch[6])
        self.assertEqual('4f031ba6c7ee9e1ded1c7c2dc5ab0bb82d239aa495e5fde55c047f09c74be901', coinbase_merkle_branch[7])
        self.assertEqual('771d47c939963f4bae3c160bfc09219f6797bb26cc66039a8798ac9e277dff2f', coinbase_merkle_branch[8])

        coinbase_merkle_index = header_auxpow['coinbase_merkle_index']
        self.assertEqual(0, coinbase_merkle_index)

        chain_merkle_branch = header_auxpow['chain_merkle_branch']
        self.assertEqual(5, len(chain_merkle_branch))
        self.assertEqual('0000000000000000000000000000000000000000000000000000000000000000', chain_merkle_branch[0])
        self.assertEqual('b886cb7e4fe65c18026bbaea7e31dfc14168b54d2b83d40bff0a240b4bcccbc1', chain_merkle_branch[1])
        self.assertEqual('58acadf5f991005ecbe697139e2ad1bc8077a3534b68604ae3a68b779908e519', chain_merkle_branch[2])
        self.assertEqual('304123c8d4cbdec14e3d16e970e8b14c87c23481fcbcff54e3ea518068960ad0', chain_merkle_branch[3])
        self.assertEqual('3ed39d3d7591968f58a6568fc7a4949aa4ca52b25b695601ea912a7290b3afb3', chain_merkle_branch[4])

        chain_merkle_index = header_auxpow['chain_merkle_index']
        self.assertEqual(8, chain_merkle_index)

        expected_parent_hash = '0000000000000074a836a521b2817a65e8a4df2dfe2c2418beb895e9cc2aa5ce'
        observed_parent_hash = blockchain.hash_header(header_auxpow['parent_header'])
        self.assertEqual(expected_parent_hash, observed_parent_hash)

        expected_parent_header = blockchain.deserialize_pure_header(bfh('00000020d4b83d5e8e6aa350094371d005275044c7789c4830b7f90200000000000000005bf56206df79280717d5d01a8f996708e55661cd960bf21875f5069a3b53ecf71fc20758c440041846f4511a'), None)
        expected_parent_merkle_root = expected_parent_header['merkle_root']
        observed_parent_merkle_root = header_auxpow['parent_header']['merkle_root']
        self.assertEqual(expected_parent_merkle_root, observed_parent_merkle_root)

    def test_deserialize_should_reject_trailing_junk(self):
        with self.assertRaises(Exception):
            self.deserialize_with_auxpow(header_850964 + "00")

    def test_deserialize_with_expected_trailing_data(self):
        data = "00" + header_850964 + "00"
        _, start_position = self.deserialize_with_auxpow(data, expect_trailing_data=True, start_position=1)
        self.assertEqual(start_position, len(header_850964)//2 + 1)

    # Verify the AuxPoW header from Terracoin block #850,964.
    def test_verify_auxpow_header_explicit_coinbase(self):
        header_bytes = bfh(header_850964)
        # We can't pass the real height because it's below a checkpoint, and
        # the deserializer expects ElectrumX to strip checkpointed AuxPoW.
        header = self.deserialize_with_auxpow(header_850964)
        blockchain.Blockchain.verify_header(header, prev_hash_850964, target_850964)

    # Verify the AuxPoW header from Terracoin block #833,204.  This header
    # doesn't have an explicit MM coinbase header.
    def test_verify_auxpow_header_implicit_coinbase(self):
        header = self.deserialize_with_auxpow(header_833204)

        blockchain.Blockchain.verify_header(header, prev_hash_833204, target_833204)

    # Check that a non-generate AuxPoW transaction is rejected.
    def test_should_reject_non_generate_auxpow(self):
        header = self.deserialize_with_auxpow(header_850964)

        header['auxpow']['coinbase_merkle_index'] = 0x01

        with self.assertRaises(auxpow.AuxPoWNotGenerateError):
            blockchain.Blockchain.verify_header(header, prev_hash_850964, target_850964)

    # Check that block headers from the sidechain are rejected as parent chain
    # for AuxPoW, via checking of the chain ID's.
    def test_should_reject_own_chain_id(self):
        parent_header = self.deserialize_with_auxpow(header_833004)
        self.assertEqual(1, auxpow.get_chain_id(parent_header))

        header = self.deserialize_with_auxpow(header_850964)
        header['auxpow']['parent_header'] = parent_header

        with self.assertRaises(auxpow.AuxPoWOwnChainIDError):
            blockchain.Blockchain.verify_header(header, prev_hash_850964, target_850964)

    # Check that where the chain merkle branch is far too long to use, it's
    # rejected.
    def test_should_reject_very_long_merkle_branch(self):
        header = self.deserialize_with_auxpow(header_850964)

        header['auxpow']['chain_merkle_branch'] = list([32 * '00' for i in range(32)])

        with self.assertRaises(auxpow.AuxPoWChainMerkleTooLongError):
            blockchain.Blockchain.verify_header(header, prev_hash_850964, target_850964)

    # Later steps in AuxPoW validation depend on the contents of the coinbase
    # transaction. Obviously that's useless if we don't check the coinbase
    # transaction is actually part of the parent chain block, so first we test
    # that the transaction hash is part of the merkle tree. This test modifies
    # the transaction, invalidating the hash, to confirm that it's rejected.
    def test_should_reject_bad_coinbase_merkle_branch(self):
        header = self.deserialize_with_auxpow(header_850964)

        # Clearing the outputs modifies the coinbase transaction so that its
        # hash no longer matches the parent block merkle root.
        self.clear_coinbase_outputs(header['auxpow'], fix_merkle_root=False)

        with self.assertRaises(auxpow.AuxPoWBadCoinbaseMerkleBranchError):
            blockchain.Blockchain.verify_header(header, prev_hash_850964, target_850964)

    # Ensure that in case of a malformed coinbase transaction (no inputs) it's
    # caught and processed neatly.
    def test_should_reject_coinbase_no_inputs(self):
        header = self.deserialize_with_auxpow(header_850964)

        # Set inputs to an empty list
        header['auxpow']['parent_coinbase_tx']._inputs = []

        self.clear_coinbase_outputs(header['auxpow'])

        with self.assertRaises(auxpow.AuxPoWCoinbaseNoInputsError):
            blockchain.Blockchain.verify_header(header, prev_hash_850964, target_850964)

    # Catch the case that the coinbase transaction does not contain details of
    # the merged block. In this case we make the transaction script too short
    # for it to do so.  This test is for the code path with an implicit MM
    # coinbase header.
    def test_should_reject_coinbase_root_too_late(self):
        header = self.deserialize_with_auxpow(header_833204)

        input_script = bfh(header['auxpow']['parent_coinbase_tx'].inputs()[0]['scriptSig'])

        padded_script = bfh('00') * (auxpow.MAX_INDEX_PC_BACKWARDS_COMPATIBILITY + 4)
        padded_script += input_script[8:]

        header['auxpow']['parent_coinbase_tx']._inputs[0]['scriptSig'] = bh2u(padded_script)

        self.clear_coinbase_outputs(header['auxpow'])

        with self.assertRaises(auxpow.AuxPoWCoinbaseRootTooLate):
            blockchain.Blockchain.verify_header(header, prev_hash_833204, target_833204)

    # Verifies that the commitment of the auxpow to the block header it is
    # proving for is actually checked.
    def test_should_reject_coinbase_root_missing(self):
        header = self.deserialize_with_auxpow(header_833204)
        # Modify the header so that its hash no longer matches the
        # chain Merkle root in the AuxPoW.
        header["timestamp"] = 42
        with self.assertRaises(auxpow.AuxPoWCoinbaseRootMissingError):
            blockchain.Blockchain.verify_header(header, prev_hash_833204, target_833204)


def update_merkle_root_to_match_coinbase(auxpow_header):
    """Updates the parent block merkle root
    This modifies the merkle root in the auxpow's parent block header to
    match the auxpow coinbase transaction.  We need this after modifying
    the coinbase for tests.
    Note that this also breaks the PoW.  This is fine for tests that
    fail due to an earlier check already."""

    coinbase = auxpow_header['parent_coinbase_tx']

    revised_coinbase_txid = auxpow.fast_txid(coinbase)
    revised_merkle_branch = [revised_coinbase_txid]
    revised_merkle_root = auxpow.calculate_merkle_root(revised_coinbase_txid, revised_merkle_branch, auxpow_header['coinbase_merkle_index'])

    auxpow_header['parent_header']['merkle_root'] = revised_merkle_root
    auxpow_header['coinbase_merkle_branch'] = revised_merkle_branch
